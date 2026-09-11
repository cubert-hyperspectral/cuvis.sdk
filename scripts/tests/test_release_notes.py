"""Folding the release notes PDF's text layer back into Markdown."""

from __future__ import annotations

import pytest

from release_notes import blocks, lines, markdown, section

# One run per (mono, text) pair, shaped exactly as pypdf hands them over: running heads
# inline, no space around the verbatim span, and the bullet hard-wrapped with hyphenation.
RUNS = [
    (False, "1 RELEASES\n1 Releases\n3.6.0\nChanges\n• Adding an option to reduce the lut using\nthe"),
    (True, "use_compressed_lut"),
    (False, "settings.\n• Various improvements for different pro-\ncessing modes.\n"),
    (False, "Page 2 of 30\nCuvis Release Notes 3.6.0\n"),
    (False, "Resolved Issues\n• Fixed a thing. It had a second sentence.\n3.5.3\nChanges\n• An older release.\n"),
]


@pytest.fixture
def document():
    return lines(RUNS)


def test_running_heads_and_folios_are_dropped(document):
    assert "Page 2 of 30" not in document
    assert "Cuvis Release Notes 3.6.0" not in document
    assert "1 RELEASES" not in document


def test_verbatim_spans_are_fenced_and_re_spaced(document):
    assert "the `use_compressed_lut` settings." in " ".join(document)


def test_section_stops_at_the_next_version(document):
    body = section(document, "3.6.0")
    assert "An older release." not in " ".join(body)
    assert "Resolved Issues" in body


def test_hyphenated_wrap_is_rejoined(document):
    assert "different processing modes." in " ".join(blocks(section(document, "3.6.0")))


def test_markdown_shape(document):
    rendered = markdown(section(document, "3.6.0"))
    assert rendered.startswith("## Changes\n")
    assert "\n\n## Resolved Issues\n" in rendered
    assert rendered.count("- ") == 3


def test_sentences_split_onto_their_own_line(document):
    """The repository writes one sentence per line; the notes follow suit."""
    assert "- Fixed a thing.\n  It had a second sentence." in markdown(section(document, "3.6.0"))


def test_a_missing_version_is_fatal(document):
    with pytest.raises(SystemExit) as failure:
        section(document, "9.9.9")
    assert "3.6.0" in str(failure.value)
