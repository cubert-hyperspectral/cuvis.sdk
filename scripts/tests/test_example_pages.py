import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from example_pages import _normalize_markdown_lists


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
