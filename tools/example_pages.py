"""Generate Python-only MkDocs pages from Cuvis SDK Jupyter notebook examples.

Parses Python Jupyter notebooks and emits prose + fenced Python code blocks
for each section. Invoked via the ``multilang_example`` macro registered in
docs_macros.py.

TODO: Re-add C and C++ code tabs once a reliable section-alignment algorithm
is available. See git history for the removed LCS-based implementation.
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_EXAMPLES_BASE = _ROOT / "examples"

# Canonical name → notebook path relative to _EXAMPLES_BASE
_EXAMPLES: dict[str, str] = {
    "Example_1_Take_Snapshot":    "cuvis.python.examples/Example_1_Take_Snapshot.ipynb",
    "Example_2_Load_Measurement": "cuvis.python.examples/Example_2_Load_Measurement.ipynb",
    "Example_3_Reprocess":        "cuvis.python.examples/Example_3_Reprocess.ipynb",
    "Example_4_Exporters":        "cuvis.python.examples/Example_4_Exporters.ipynb",
    "Example_5_Record_Video":     "cuvis.python.examples/Example_5_Record_Video.ipynb",
}


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
# Output formatting
# ---------------------------------------------------------------------------

def _format_section(prose: str, py_code: str) -> str:
    """Combine prose and a fenced Python code block into one page section."""
    parts: list[str] = []

    if prose.strip():
        parts.append(prose.strip())

    if py_code.strip():
        code = textwrap.dedent(py_code).strip()
        parts.append(f"```python\n{code}\n```")

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def multilang_example(name: str) -> str:
    """Return full MkDocs markdown for an example page (Python only).

    *name* must be one of the keys in ``_EXAMPLES`` (e.g. ``"Example_2_Load_Measurement"``).
    A missing notebook produces a warning admonition rather than raising.

    TODO: Re-add C and C++ code tabs once a reliable section-alignment
    algorithm is in place. The previous LCS-based approach produced
    incorrect matches for structural mismatches (e.g. per-mode Python
    sections vs. a single loop in C++). See git history for the removed
    implementation.
    """
    nb_rel = _EXAMPLES.get(name)
    if not nb_rel:
        known = ", ".join(f"`{k}`" for k in _EXAMPLES)
        return f"!!! failure\n    Unknown example `{name}`. Known examples: {known}\n"

    nb_path = _EXAMPLES_BASE / nb_rel
    if not nb_path.exists():
        return f"!!! warning\n    Notebook not found: `{nb_path}`\n"

    py_sections = _parse_notebook(nb_path)
    page_sections = [
        _format_section(prose, py_code)
        for prose, py_code in py_sections
        if prose.strip() or py_code.strip()
    ]
    return "\n\n---\n\n".join(page_sections)
