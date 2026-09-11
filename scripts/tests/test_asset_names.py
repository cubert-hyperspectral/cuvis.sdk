"""The naming grammar: share folders in, release asset names out."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from asset_names import (
    ASSET,
    FOLDER,
    SOURCE,
    asset_name,
    barren,
    metadata_name,
    recognised,
    staged,
    unparsed,
)

# The nine variant folders the 3.6.0 share actually ships, plus the shapes 3.5.3 used.
FOLDERS_360 = (
    "Ubuntu 22.04-amd64-cuda12.9",
    "Ubuntu 22.04-amd64-cudano",
    "Ubuntu 22.04-arm64-cuda12.2-jetson",
    "Ubuntu 24.04-amd64-cuda12.9",
    "Ubuntu 24.04-amd64-cudano",
    "Ubuntu 24.04-arm64-cuda13.2-jetson",
    "Ubuntu 26.04-amd64-cuda13.3",
    "Ubuntu 26.04-amd64-cudano",
    "Windows amd64-cuda12.9",
)
FOLDERS_353 = (
    "Ubuntu 20.04-amd64-nocuda",
    "Ubuntu 22.04-arm64-cuda11.8-jetson-experimental",
    "Windows amd64-cuda12.3",
)

NAMED = {
    ("Ubuntu 24.04-amd64-cudano", "libcuvis_3.6.0-0.deb"): "libcuvis_3.6.0-0_Ubuntu24.04_amd64_nocuda.deb",
    ("Ubuntu 24.04-amd64-nocuda", "libcuvis_3.6.0-0.deb"): "libcuvis_3.6.0-0_Ubuntu24.04_amd64_nocuda.deb",
    ("Ubuntu 24.04-arm64-cuda13.2-jetson", "cuviscommon_3.6.0-0.deb"): "cuviscommon_3.6.0-0_Ubuntu24.04-jetson_arm64_cuda13.2.deb",
    ("Ubuntu 22.04-arm64-cuda11.8-jetson-experimental", "libcuvis_3.5.3-0.deb"): "libcuvis_3.5.3-0_Ubuntu22.04-jetson-experimental_arm64_cuda11.8.deb",
    ("Ubuntu 26.04-amd64-cuda13.3", "libcuvis_3.6.0-0.deb"): "libcuvis_3.6.0-0_Ubuntu26.04_amd64_cuda13.3.deb",
    ("Windows amd64-cuda12.9", "Cuvis_C_SDK_Installer_3.6.0.exe"): "Cuvis_C_SDK_Installer_3.6.0_Windows_amd64_cuda12.9.exe",
}


@pytest.mark.parametrize("folder", FOLDERS_360 + FOLDERS_353)
def test_every_shipped_folder_parses(folder):
    assert FOLDER.fullmatch(folder), folder


@pytest.mark.parametrize(("folder", "source"), NAMED)
def test_asset_name(folder, source):
    """cudano normalises to nocuda; the jetson suffix rides along in the os token."""
    assert asset_name(FOLDER.fullmatch(folder), SOURCE.fullmatch(source)) == NAMED[folder, source]


@pytest.mark.parametrize("source", ["libcuvis_3.6.0-0.deb", "cuviscommon_3.6.0-0.deb", "Cuvis_C_SDK_Installer_3.6.0.exe"])
def test_package_version_survives_the_debian_revision(source):
    assert SOURCE.fullmatch(source)["pkgver"].startswith("3.6.0")


def test_names_round_trip_through_the_asset_pattern():
    assert all(ASSET.fullmatch(name) for name in NAMED.values())


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Release Notes.pdf", "RELEASE-NOTES_v3.6.0.pdf"),
        ("Application_Notes_Cuvis_SDK_Linux.pdf", "Application-Notes_Cuvis-SDK_Linux.pdf"),
        ("SHA256SUMS.txt", None),
    ],
)
def test_metadata_name(name, expected):
    assert metadata_name(name, "3.6.0") == expected


def share(root: Path, folders, packages=("libcuvis_3.6.0-0.deb", "cuviscommon_3.6.0-0.deb")) -> Path:
    for folder in folders:
        directory = root / folder
        directory.mkdir(parents=True)
        for package in packages:
            (directory / package).write_bytes(b"x")
    return root


def test_staged_covers_every_folder(tmp_path):
    plan = staged(share(tmp_path, FOLDERS_360[:3]), "3.6.0")
    assert len(plan) == 6
    assert all(recognised(name) for name in plan.values())


def test_unparsed_reports_unknown_folders(tmp_path):
    (tmp_path / "not a variant").mkdir()
    assert unparsed(share(tmp_path, FOLDERS_360[:1])) == ["not a variant"]


def test_barren_reports_a_folder_whose_build_produced_nothing(tmp_path):
    share(tmp_path, FOLDERS_360[:1])
    (tmp_path / FOLDERS_360[1]).mkdir()
    assert barren(tmp_path) == [FOLDERS_360[1]]


def selector_pattern() -> re.Pattern[str]:
    """The copy of Pattern A the docs selector parses the Releases API with."""
    selector = Path(__file__).resolve().parents[2] / "docs/javascripts/sdk-installer.js"
    literal = re.search(r"RX_INSTALLER\s*=\s*/(?P<body>.+)/;", selector.read_text(encoding="utf-8"))
    assert literal, "RX_INSTALLER not found in the selector"
    # JavaScript spells a named group (?<name>...), Python (?P<name>...).
    return re.compile(re.sub(r"\(\?<(?=[A-Za-z])", "(?P<", literal["body"]))


def test_docs_selector_accepts_every_published_name():
    pattern = selector_pattern()
    assert all(pattern.fullmatch(name) for name in NAMED.values())


def test_every_share_folder_becomes_a_complete_selectable_option(tmp_path):
    """Names that parse are not enough: each variant must offer a usable download."""
    windows, ubuntu = ["Cuvis_C_SDK_Installer_3.6.0.exe"], ["libcuvis_3.6.0-0.deb", "cuviscommon_3.6.0-0.deb"]
    for folder in FOLDERS_360:
        share(tmp_path, [folder], windows if folder.startswith("Windows") else ubuntu)

    pattern = selector_pattern()
    parsed = [pattern.fullmatch(name) for name in staged(tmp_path, "3.6.0").values()]
    assert all(parsed), "the selector cannot parse a name the stager produced"

    # osBucket() and cudaLabel() in docs/javascripts/sdk-installer.js.
    offered: dict[tuple[str, str, str], set[str]] = {}
    for match in parsed:
        key = (match["os"], match["arch"], match["cuda"])
        offered.setdefault(key, set()).add(match["pkg"])

    assert len(offered) == len(FOLDERS_360)
    assert all(cuda != "cudano" for _, _, cuda in offered), "cudano would render as a literal dropdown label"
    for (os_name, _, _), packages in offered.items():
        expected = {"Cuvis_C_SDK_Installer"} if os_name == "Windows" else {"libcuvis", "cuviscommon"}
        assert packages == expected, f"{os_name} offers {packages}"
