"""Tests for cuvis_sdk_url.

Mocks `urllib.request.urlopen` to feed canned GitHub API responses; verifies
regex matches, version-resolution defaults, prerelease filtering, the Linux
.deb-pair handling, and the LookupError edge cases.
"""

from __future__ import annotations

import io
import json
from unittest.mock import patch

import pytest

import cuvis_sdk_url
from cuvis_sdk_url import (
    REGEX_INSTALLER,
    REGEX_METADATA,
    install_command,
    list_release_metadata,
    sdk_url,
    sdk_urls,
)

WIN_ASSET = "Cuvis_C_SDK_Installer_3.5.3_Windows_amd64_cuda12.3.exe"
LIB_ASSET = "libcuvis_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb"
COM_ASSET = "cuviscommon_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb"
JET_LIB = "libcuvis_3.5.3-0_Ubuntu22.04-jetson-experimental_arm64_cuda13.0.deb"
JET_COM = "cuviscommon_3.5.3-0_Ubuntu22.04-jetson-experimental_arm64_cuda13.0.deb"
PDF = "RELEASE-NOTES_v3.5.3.pdf"
APP_PDF = "Application-Notes_Cuvis-SDK_Linux.pdf"
SUMS = "SHA256SUMS.txt"
SHA_SIDECAR = WIN_ASSET + ".sha256"


@pytest.fixture(autouse=True)
def _clear_cache():
    cuvis_sdk_url._cache.clear()
    yield
    cuvis_sdk_url._cache.clear()


def _release(tag, prerelease=False, asset_names=()):
    return {
        "tag_name": tag,
        "prerelease": prerelease,
        "assets": [
            {"name": n, "browser_download_url": f"https://example/{tag}/{n}"}
            for n in asset_names
        ],
    }


def _patch_releases(payload):
    body = json.dumps(payload).encode("utf-8")

    class FakeResp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return body

    return patch.object(
        cuvis_sdk_url.urllib.request, "urlopen", return_value=FakeResp()
    )


def _full_release(tag="v3.5.3", prerelease=False):
    return _release(
        tag,
        prerelease,
        [WIN_ASSET, LIB_ASSET, COM_ASSET, JET_LIB, JET_COM, PDF, APP_PDF, SUMS, SHA_SIDECAR],
    )


# --- Regex tests ----------------------------------------------------------


class TestRegexes:
    def test_pattern_a_windows(self):
        m = REGEX_INSTALLER.match(WIN_ASSET)
        assert m
        assert m.group("pkg") == "Cuvis_C_SDK_Installer"
        assert m.group("pkgver") == "3.5.3"
        assert m.group("os") == "Windows"
        assert m.group("arch") == "amd64"
        assert m.group("cuda") == "cuda12.3"
        assert m.group("ext") == "exe"

    def test_pattern_a_ubuntu(self):
        assert REGEX_INSTALLER.match(LIB_ASSET)
        assert REGEX_INSTALLER.match(COM_ASSET)

    def test_pattern_a_jetson_experimental(self):
        m = REGEX_INSTALLER.match(JET_LIB)
        assert m
        assert m.group("os") == "Ubuntu22.04-jetson-experimental"
        assert m.group("arch") == "arm64"
        assert m.group("cuda") == "cuda13.0"

    def test_pkgver_carries_debian_revision(self):
        assert REGEX_INSTALLER.match(LIB_ASSET).group("pkgver") == "3.5.3-0"

    def test_pkgver_without_debian_revision(self):
        assert REGEX_INSTALLER.match(WIN_ASSET).group("pkgver") == "3.5.3"

    def test_pattern_b_pdf(self):
        assert REGEX_METADATA.match(PDF)
        assert REGEX_METADATA.match(APP_PDF)

    def test_pattern_b_sums(self):
        assert REGEX_METADATA.match(SUMS)

    def test_pattern_b_sha256_sidecar(self):
        assert REGEX_METADATA.match(SHA_SIDECAR)
        # Sidecars must NOT also match Pattern A.
        assert not REGEX_INSTALLER.match(SHA_SIDECAR)

    def test_unmatched_name_fails_both(self):
        bad = "notes.txt"
        assert not REGEX_INSTALLER.match(bad)
        assert not REGEX_METADATA.match(bad)


# --- sdk_urls -------------------------------------------------------------


class TestSdkUrls:
    def test_windows_resolves_single_installer(self):
        with _patch_releases([_full_release()]):
            urls = sdk_urls(os="Windows", arch="amd64", cuda="cuda12.3")
        assert set(urls) == {"installer"}
        assert urls["installer"].endswith(WIN_ASSET)

    def test_ubuntu_resolves_deb_pair(self):
        with _patch_releases([_full_release()]):
            urls = sdk_urls(os="Ubuntu24.04", arch="amd64", cuda="nocuda")
        assert set(urls) == {"libcuvis", "cuviscommon"}

    def test_jetson_arm64_cuda(self):
        with _patch_releases([_full_release()]):
            urls = sdk_urls(
                os="Ubuntu22.04-jetson-experimental",
                arch="arm64",
                cuda="cuda13.0",
            )
        assert set(urls) == {"libcuvis", "cuviscommon"}

    def test_no_match_raises_lookup_error(self):
        with _patch_releases([_full_release()]):
            with pytest.raises(LookupError):
                sdk_urls(os="macOS", arch="amd64", cuda="cuda12.3")

    def test_specific_version(self):
        old = _release(
            "v3.5.0",
            asset_names=["Cuvis_C_SDK_Installer_3.5.0_Windows_amd64_cuda12.3.exe"],
        )
        with _patch_releases([_full_release("v3.5.3"), old]):
            urls = sdk_urls(
                os="Windows", arch="amd64", cuda="cuda12.3", version="v3.5.0"
            )
        assert "v3.5.0" in urls["installer"]
        assert "3.5.0" in urls["installer"]

    def test_default_version_is_first(self):
        # GitHub returns newest-first; helper picks the first non-prerelease.
        old = _release(
            "v3.5.0",
            asset_names=["Cuvis_C_SDK_Installer_3.5.0_Windows_amd64_cuda12.3.exe"],
        )
        with _patch_releases([_full_release("v3.5.3"), old]):
            urls = sdk_urls(os="Windows", arch="amd64", cuda="cuda12.3")
        assert "v3.5.3" in urls["installer"]

    def test_unknown_version_raises(self):
        with _patch_releases([_full_release("v3.5.3")]):
            with pytest.raises(LookupError):
                sdk_urls(
                    os="Windows", arch="amd64", cuda="cuda12.3", version="v9.9.9"
                )

    def test_prerelease_filtered_by_default(self):
        pre = _release(
            "v3.6.0-rc1",
            prerelease=True,
            asset_names=["Cuvis_C_SDK_Installer_3.6.0_Windows_amd64_cuda12.3.exe"],
        )
        with _patch_releases([pre, _full_release("v3.5.3")]):
            urls = sdk_urls(os="Windows", arch="amd64", cuda="cuda12.3")
        assert "v3.5.3" in urls["installer"]

    def test_prerelease_included_on_demand(self):
        pre = _release(
            "v3.6.0-rc1",
            prerelease=True,
            asset_names=["Cuvis_C_SDK_Installer_3.6.0_Windows_amd64_cuda12.3.exe"],
        )
        with _patch_releases([pre, _full_release("v3.5.3")]):
            urls = sdk_urls(
                os="Windows",
                arch="amd64",
                cuda="cuda12.3",
                include_prerelease=True,
            )
        assert "v3.6.0-rc1" in urls["installer"]


# --- sdk_url --------------------------------------------------------------


class TestSdkUrl:
    def test_default_package_installer(self):
        with _patch_releases([_full_release()]):
            url = sdk_url(os="Windows", arch="amd64", cuda="cuda12.3")
        assert url.endswith(WIN_ASSET)

    def test_explicit_libcuvis(self):
        with _patch_releases([_full_release()]):
            url = sdk_url(
                os="Ubuntu24.04",
                arch="amd64",
                cuda="nocuda",
                package="libcuvis",
            )
        assert url.endswith(LIB_ASSET)

    def test_unknown_package_raises(self):
        with _patch_releases([_full_release()]):
            with pytest.raises(LookupError, match="libcuvis"):
                sdk_url(
                    os="Windows",
                    arch="amd64",
                    cuda="cuda12.3",
                    package="libcuvis",
                )


# --- install_command ------------------------------------------------------


class TestInstallCommand:
    def test_ubuntu_three_line_command(self):
        with _patch_releases([_full_release()]):
            cmd = install_command(os="Ubuntu24.04", arch="amd64", cuda="nocuda")
        lines = cmd.splitlines()
        assert len(lines) == 3
        # cuviscommon installs first, libcuvis second.
        assert "cuviscommon" in lines[0] and lines[0].startswith("curl -O ")
        assert "libcuvis" in lines[1] and lines[1].startswith("curl -O ")
        assert lines[2] == "sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb"

    def test_windows_two_line_command(self):
        with _patch_releases([_full_release()]):
            cmd = install_command(os="Windows", arch="amd64", cuda="cuda12.3")
        lines = cmd.splitlines()
        assert len(lines) == 2
        assert lines[0].startswith("Invoke-WebRequest")
        assert "Start-Process" in lines[1]


# --- list_release_metadata -----------------------------------------------


class TestListReleaseMetadata:
    def test_returns_pattern_b_only(self):
        with _patch_releases([_full_release()]):
            meta = list_release_metadata()
        assert PDF in meta
        assert APP_PDF in meta
        assert SUMS in meta
        # Pattern A binaries must NOT be listed even though `.+\.pdf` is broad.
        assert WIN_ASSET not in meta
        assert LIB_ASSET not in meta


# --- caching --------------------------------------------------------------


class TestCaching:
    def test_repeated_calls_share_cache(self):
        with _patch_releases([_full_release()]) as mock_open:
            sdk_urls(os="Windows", arch="amd64", cuda="cuda12.3")
            sdk_urls(os="Ubuntu24.04", arch="amd64", cuda="nocuda")
            list_release_metadata()
        assert mock_open.call_count == 1
