"""Generate multi-language tabbed MkDocs pages from Cuvis SDK example sources.

Parses Python Jupyter notebooks and C/C++ source files, aligns sections by
keyword similarity between notebook markdown cells and C block comments, then
emits a pymdownx.tabbed page with interleaved prose and language-switched code
blocks. Invoked via the ``multilang_example`` macro registered in docs_macros.py.
"""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_EXAMPLES_BASE = _ROOT / "examples"

# Canonical name → paths relative to _EXAMPLES_BASE
_EXAMPLES: dict[str, dict[str, str]] = {
    "Example_1_Take_Snapshot": {
        "nb": "cuvis.python.examples/Example_1_Take_Snapshot.ipynb",
        "c": "cuvis.c.examples/Example_1_Take_Snapshot/main.c",
        "cpp": "cuvis.cpp.examples/Example_1_Take_Snapshot_cpp/main.cpp",
    },
    "Example_2_Load_Measurement": {
        "nb": "cuvis.python.examples/Example_2_Load_Measurement.ipynb",
        "c": "cuvis.c.examples/Example_2_Load_Measurement/main.c",
        "cpp": "cuvis.cpp.examples/Example_2_Load_Measurement_cpp/main.cpp",
    },
    "Example_3_Reprocess": {
        "nb": "cuvis.python.examples/Example_3_Reprocess.ipynb",
        "c": "cuvis.c.examples/Example_3_Reprocess/main.c",
        "cpp": "cuvis.cpp.examples/Example_3_Reprocess_cpp/main.cpp",
    },
    "Example_4_Exporters": {
        "nb": "cuvis.python.examples/Example_4_Exporters.ipynb",
        "c": "cuvis.c.examples/Example_4_Exporters/main.c",
        "cpp": "cuvis.cpp.examples/Example_4_Exporters_cpp/main.cpp",
    },
    "Example_5_Record_Video": {
        "nb": "cuvis.python.examples/Example_5_Record_Video.ipynb",
        "c": "cuvis.c.examples/Example_5_Record_Video/main.c",
        "cpp": "cuvis.cpp.examples/Example_5_Record_Video_cpp/main.cpp",
    },
}

_STOPWORDS = frozenset(
    "this that with from have will more than some into used about also only "
    "note please both each when then here just your also after before first "
    "last which their there these those".split()
)


# ---------------------------------------------------------------------------
# Notebook parsing
# ---------------------------------------------------------------------------

def _parse_notebook(nb_path: Path) -> list[tuple[str, str]]:
    """Return list of (prose, code) sections from a Jupyter notebook.

    A new section begins at each markdown cell. All code cells that follow
    (until the next markdown cell) are joined as the section's code block.
    Cells with no source are skipped.
    """
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)

    sections: list[tuple[str, str]] = []
    pending_prose: list[str] = []
    pending_code: list[str] = []

    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", [])).strip()
        if not src:
            continue
        ctype = cell.get("cell_type", "")

        if ctype == "markdown":
            if pending_code:
                sections.append(("\n\n".join(pending_prose), "\n\n".join(pending_code)))
                pending_prose = []
                pending_code = []
            pending_prose.append(src)
        elif ctype == "code":
            pending_code.append(src)

    if pending_code:
        sections.append(("\n\n".join(pending_prose), "\n\n".join(pending_code)))

    return sections


# ---------------------------------------------------------------------------
# C / C++ parsing
# ---------------------------------------------------------------------------

def _clean_block_comment(raw: str) -> str:
    """Strip leading `*` chars from each line of a C block comment interior."""
    lines = [re.sub(r"^\s*\*\s?", "", line) for line in raw.splitlines()]
    return "\n".join(lines).strip()


def _strip_unbalanced_brace(code: str) -> str:
    """Remove one trailing `}` when closing braces outnumber opening ones.

    Handles the C++ pattern where main() wraps its body in an extra ``{ }``
    block: after stripping main()'s own closing brace, the extra brace shows
    up as the last character of the final code section.
    """
    if code.count("}") > code.count("{"):
        idx = code.rfind("}")
        code = (code[:idx] + code[idx + 1 :]).strip()
    return code


def _parse_c_source(src_path: Path) -> list[tuple[str, str]]:
    """Return list of (comment_text, following_code) pairs from a C/C++ file.

    Extracts the body of ``main()``, then splits on ``/* … */`` block comments.
    Each comment + the code that immediately follows it becomes one pair.
    """
    with open(src_path, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Locate main() and take its body
    main_m = re.search(r"int\s+main\s*\([^)]*\)\s*\{", content)
    if not main_m:
        return []

    body = content[main_m.end() :]
    # Strip the outermost closing `}` of main()
    last_brace = body.rfind("}")
    if last_brace >= 0:
        body = body[:last_brace]

    # Split on /* … */ block comments; capturing group yields alternating
    # [code, comment, code, comment, …]
    parts = re.split(r"/\*(.*?)\*/", body, flags=re.DOTALL)

    pairs: list[tuple[str, str]] = []
    for i in range(1, len(parts), 2):
        comment = _clean_block_comment(parts[i])
        raw_code = parts[i + 1] if i + 1 < len(parts) else ""
        code = textwrap.dedent(raw_code).strip()
        code = _strip_unbalanced_brace(code)

        if comment or code:
            pairs.append((comment, code))

    return pairs


# ---------------------------------------------------------------------------
# Section matching
# ---------------------------------------------------------------------------

def _keywords(text: str) -> frozenset[str]:
    """Return set of significant lowercase words (≥4 chars) from *text*."""
    clean = re.sub(r"[#*_`\[\]()!]", " ", text)
    words = re.findall(r"\b[a-z]{4,}\b", clean.lower())
    return frozenset(w for w in words if w not in _STOPWORDS)


def _section_heading(prose: str) -> str:
    """Extract the most specific heading line from markdown prose."""
    for pattern in (r"#{4}\s+(.+)$", r"#{3}\s+(.+)$", r"#{2}\s+(.+)$", r"#{1}\s+(.+)$"):
        m = re.search(pattern, prose, re.MULTILINE)
        if m:
            return m.group(1)
    return prose.split("\n")[0]


def _section_score(py_prose: str, c_comment: str) -> int:
    """Score how well a C comment matches a Python prose section.

    The first line of the C comment (the section title) is weighted 3× vs the
    full-body keyword overlap, so "SessionFile" / "Measurement" headings match
    their counterparts precisely instead of tying on incidental body mentions.
    """
    py_heading_kw = _keywords(_section_heading(py_prose))
    if not py_heading_kw:
        return 0

    c_first_line_kw = _keywords(c_comment.split("\n")[0])
    c_body_kw = _keywords(c_comment[:400])

    primary = len(py_heading_kw & c_first_line_kw) * 3
    secondary = len(py_heading_kw & c_body_kw)
    return primary + secondary


def _match_c_sections(
    py_sections: list[tuple[str, str]],
    c_pairs: list[tuple[str, str]],
) -> dict[int, str]:
    """Map each C pair to the best-matching Python section index.

    Matching is keyword-based and order-preserving: once a C pair is matched
    to Python section *k*, the next C pair can only match section *k* or later.
    Unmatched C pairs (score = 0) are folded into the most-recently matched
    Python section so their code isn't lost.

    Returns ``{py_index: combined_c_code}``.
    """
    result: dict[int, list[str]] = {i: [] for i in range(len(py_sections))}
    last_matched = 0

    for c_comment, c_code in c_pairs:
        if not c_code:
            continue

        best_idx: int | None = None
        best_score = 0

        # Only search at or after the last matched position (preserves order)
        for py_idx in range(last_matched, len(py_sections)):
            py_prose, _ = py_sections[py_idx]
            if not py_prose.strip():
                continue
            score = _section_score(py_prose, c_comment)
            if score > best_score:
                best_score = score
                best_idx = py_idx

        if best_idx is not None and best_score > 0:
            result[best_idx].append(c_code)
            last_matched = best_idx
        else:
            # No keyword match — append to the currently active Python section
            result[last_matched].append(c_code)

    return {k: "\n\n".join(v) for k, v in result.items() if v}


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def _code_tab(label: str, lang: str, code: str) -> str:
    """Return a single pymdownx.tabbed tab block, or empty string if no code."""
    if not code.strip():
        return ""
    fence = f"```{lang}\n{code.strip()}\n```"
    # pymdownx.tabbed requires 4-space indent for content
    indented = "\n".join("    " + line for line in fence.splitlines())
    return f'=== "{label}"\n\n{indented}\n'


def _format_section(prose: str, py_code: str, c_code: str, cpp_code: str) -> str:
    """Combine prose and a three-language tab block into one page section."""
    parts: list[str] = []

    if prose.strip():
        parts.append(prose.strip())

    tabs = [
        _code_tab("Python", "python", py_code),
        _code_tab("C", "c", c_code),
        _code_tab("C++", "cpp", cpp_code),
    ]
    non_empty_tabs = [t for t in tabs if t]
    if non_empty_tabs:
        parts.append("\n\n".join(non_empty_tabs))

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def multilang_example(name: str) -> str:
    """Return full MkDocs markdown for a multi-language example page.

    *name* must be one of the keys in ``_EXAMPLES`` (e.g. ``"Example_2_Load_Measurement"``).
    Missing source files produce a warning admonition rather than raising.
    """
    info = _EXAMPLES.get(name)
    if not info:
        known = ", ".join(f"`{k}`" for k in _EXAMPLES)
        return f"!!! failure\n    Unknown example `{name}`. Known examples: {known}\n"

    nb_path = _EXAMPLES_BASE / info["nb"]
    c_path = _EXAMPLES_BASE / info["c"]
    cpp_path = _EXAMPLES_BASE / info["cpp"]

    missing = [str(p) for p in (nb_path, c_path, cpp_path) if not p.exists()]
    if missing:
        files = "\n".join(f"    - `{p}`" for p in missing)
        return f"!!! warning\n    Source files not found:\n{files}\n"

    py_sections = _parse_notebook(nb_path)
    c_pairs = _parse_c_source(c_path)
    cpp_pairs = _parse_c_source(cpp_path)

    c_map = _match_c_sections(py_sections, c_pairs)
    cpp_map = _match_c_sections(py_sections, cpp_pairs)

    page_sections: list[str] = []
    for i, (prose, py_code) in enumerate(py_sections):
        c_code = c_map.get(i, "")
        cpp_code = cpp_map.get(i, "")
        section = _format_section(prose, py_code, c_code, cpp_code)
        if section.strip():
            page_sections.append(section)

    return "\n\n---\n\n".join(page_sections)
