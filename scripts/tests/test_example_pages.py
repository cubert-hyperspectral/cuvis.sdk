import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import example_pages
from example_pages import _normalize_markdown_lists, _parse_notebook, multilang_example


def _write_notebook(path: Path, cells: list[tuple[str, str]]) -> Path:
    """Write a minimal .ipynb with the given ``(cell_type, source)`` cells."""
    nb = {"cells": [{"cell_type": ctype, "source": src} for ctype, src in cells]}
    path.write_text(json.dumps(nb), encoding="utf-8")
    return path


def test_adds_blank_line_before_bullet_list():
    prose = "**Used principles:**\n - *AcquisitionContext* for camera control"

    assert _normalize_markdown_lists(prose) == (
        "**Used principles:**\n"
        "\n"
        " - *AcquisitionContext* for camera control"
    )


def test_adds_blank_line_before_ordered_list():
    prose = "**Step-by-Step outline:**\n 1. Import and initialize Cuvis SDK"

    assert _normalize_markdown_lists(prose) == (
        "**Step-by-Step outline:**\n"
        "\n"
        " 1. Import and initialize Cuvis SDK"
    )


def test_does_not_duplicate_existing_blank_line():
    prose = "**Used principles:**\n\n - *SessionFile* as camera calibration file"

    assert _normalize_markdown_lists(prose) == prose


def test_nested_list_items_stay_attached_to_parent_list():
    prose = "- parent\n  - child"

    assert _normalize_markdown_lists(prose) == prose


def test_fenced_code_content_is_untouched():
    prose = "Example:\n```\nnot a list\n - keep this inside the fence\n```\nAfter"

    assert _normalize_markdown_lists(prose) == prose


def test_parse_notebook_groups_prose_with_following_code(tmp_path):
    nb = _write_notebook(
        tmp_path / "nb.ipynb",
        [("markdown", "# Intro"), ("code", "x = 1"),
         ("markdown", "## Step"), ("code", "y = 2")],
    )

    assert _parse_notebook(nb) == [("# Intro", "x = 1"), ("## Step", "y = 2")]


def test_parse_notebook_keeps_trailing_markdown_without_code(tmp_path):
    nb = _write_notebook(
        tmp_path / "nb.ipynb",
        [("markdown", "# Intro"), ("code", "x = 1"), ("markdown", "## Conclusion")],
    )

    # A notebook ending in a markdown cell must not lose its closing prose.
    assert _parse_notebook(nb) == [("# Intro", "x = 1"), ("## Conclusion", "")]


def test_parse_notebook_skips_empty_cells(tmp_path):
    nb = _write_notebook(
        tmp_path / "nb.ipynb",
        [("markdown", ""), ("code", "   "), ("markdown", "# Title"), ("code", "z = 3")],
    )

    assert _parse_notebook(nb) == [("# Title", "z = 3")]


def test_multilang_example_unknown_name_returns_failure_admonition():
    out = multilang_example("Not_A_Real_Example")

    assert out.startswith("!!! failure")
    assert "Not_A_Real_Example" in out


def test_multilang_example_missing_notebook_returns_warning(tmp_path, monkeypatch):
    monkeypatch.setattr(example_pages, "_EXAMPLES_BASE", tmp_path)
    monkeypatch.setattr(example_pages, "_EXAMPLES", {"Ghost": "does_not_exist.ipynb"})

    out = multilang_example("Ghost")

    assert out.startswith("!!! warning")
