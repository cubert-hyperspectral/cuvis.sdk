#!/usr/bin/env python3
"""Extract one version's section from the SDK release notes PDF as Markdown.

    python scripts/release_notes.py --version 3.6.0 --pdf "_assets/Cuvis 3.6.0/Release Notes.pdf"

The PDF is cumulative, newest version first, and typeset with LaTeX. Two things about its
text layer drive the shape of this module:

- It emits no space around a verbatim span, so "the use_compressed_lut settings" arrives as
  "theuse_compressed_lutsettings". The spans are recoverable because they carry their own
  typewriter font, which is also what lets them be fenced in backticks.
- Paragraphs are hard-wrapped with hyphenation, so bullets arrive split across lines.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MONO = re.compile(r"TT\d|Mono|Courier|Typewriter")
BULLET = "•"
VERSION = re.compile(r"\d+\.\d+\.\d+")
SUBSECTIONS = ("Changes", "Resolved Issues", "Known Issues")

# Running heads, folios and the table of contents, which sit inline in the text layer.
FURNITURE = re.compile(
    r"Page \d+ of \d+|Cuvis Release Notes [\d.]+|\d+ RELEASES?|\d+ Releases"
    r"|Contents|Cuvis|Release Notes|\d+ Support|Support"
)

SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(])")


def spans(pdf: Path) -> list[tuple[bool, str]]:
    """Every text run in the document, flagged with whether it is set in the mono font."""
    from pypdf import PdfReader

    runs: list[tuple[bool, str]] = []

    def visit(text, _cm, _tm, font, _size):
        if text:
            runs.append((bool(font and MONO.search(str(font.get("/BaseFont")))), text))

    for page in PdfReader(pdf).pages:
        page.extract_text(visitor_text=visit)
    return runs


def lines(runs: list[tuple[bool, str]]) -> list[str]:
    """The document as clean single-spaced lines, verbatim spans fenced and re-spaced."""
    document = "".join(f" `{text.strip()}` " if mono and text.strip() else text for mono, text in runs)
    return [
        squeezed
        for line in document.splitlines()
        if (squeezed := " ".join(line.split())) and not FURNITURE.fullmatch(squeezed)
    ]


def section(document: list[str], version: str) -> list[str]:
    """The lines belonging to one version, up to the next version heading."""
    start = next((i for i, line in enumerate(document) if line == version), None)
    if start is None:
        found = [line for line in document if VERSION.fullmatch(line)]
        sys.exit(f"the release notes have no section for {version}; they carry {', '.join(found[:5]) or 'none'}")
    rest = document[start + 1:]
    end = next((i for i, line in enumerate(rest) if VERSION.fullmatch(line)), len(rest))
    return rest[:end]


def blocks(body: list[str]) -> list[str]:
    out: list[str] = []
    for line in body:
        if line in SUBSECTIONS:
            out.append(f"## {line}")
        elif line.startswith(BULLET):
            out.append(line[1:].strip())
        elif out and not out[-1].startswith("## "):
            # A continuation: de-hyphenate the word the typesetter split across the wrap.
            out[-1] = out[-1][:-1] + line if out[-1].endswith("-") else f"{out[-1]} {line}"
    return out


def markdown(body: list[str]) -> str:
    """One sentence per line, the convention the changelog and these notes already follow."""
    rendered = "\n".join(
        block
        if block.startswith("## ")
        else "\n  ".join(f"- {s}" if i == 0 else s for i, s in enumerate(SENTENCE.split(block)))
        for block in blocks(body)
    )
    return re.sub(r"\n(## )", r"\n\n\1", rendered).strip() + "\n"


def notes(pdf: Path, version: str) -> str:
    if not pdf.is_file():
        sys.exit(f"{pdf} does not exist; the share must carry the release notes for {version}")
    return markdown(section(lines(spans(pdf)), version))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", required=True, help="SDK version, e.g. 3.6.0")
    parser.add_argument("--pdf", type=Path, help="release notes PDF (default: the one in the share tree)")
    parser.add_argument("--source", type=Path, default=Path("_assets"), help="directory holding 'Cuvis <version>'")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf = args.pdf or args.source / f"Cuvis {args.version}" / "Release Notes.pdf"
    print(notes(pdf, args.version))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
