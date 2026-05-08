# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Resolve Cuvis SDK release-asset URLs from GitHub Releases.

Two consumption modes (pure stdlib — urllib.request, json, re, time, argparse):

- **CLI** (primary). Run via `uv run scripts/cuvis_sdk_url.py <subcommand>`:

    uv run scripts/cuvis_sdk_url.py urls --os Ubuntu24.04
    uv run scripts/cuvis_sdk_url.py install-command --os Windows --cuda cuda12.3
    uv run scripts/cuvis_sdk_url.py url --os Ubuntu24.04 --package libcuvis
    uv run scripts/cuvis_sdk_url.py metadata --version v3.5.3

- **Imported as a Python module from inside this repo** by `tools/docs_macros.py`
  to render `{{ cuvis_install_command(os="Ubuntu24.04") }}` at mkdocs build time
  as the noscript fallback on the selector page. tools/docs_macros.py adds
  this directory to `sys.path` before the import.

Exported regexes: REGEX_INSTALLER (Pattern A), REGEX_METADATA (Pattern B) —
identical to the patterns in scripts/lint-release-assets.ps1 and the JS
selector. If you change one, update the other two.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from typing import Any

REPO = "cubert-hyperspectral/cuvis.sdk"
RELEASES_URL = f"https://api.github.com/repos/{REPO}/releases?per_page=100"

# Pattern A — installers/packages (drives the selector dropdowns).
REGEX_INSTALLER = re.compile(
    r"^(?P<pkg>Cuvis_C_SDK_Installer|libcuvis|cuviscommon)"
    r"_(?P<pkgver>[0-9.]+(?:-[0-9]+)?)"
    r"_(?P<os>Windows|macOS|Ubuntu[0-9.]+(?:-jetson(?:-experimental)?)?)"
    r"_(?P<arch>amd64|arm64)"
    r"_(?P<cuda>nocuda|cuda[0-9.]+)"
    r"\.(?P<ext>exe|deb|msi|dmg|pkg|tar\.gz)$"
)

# Pattern B — release metadata (allowed in the release, not in the dropdowns).
REGEX_METADATA = re.compile(
    r"^(SHA256SUMS\.txt|.+\.sha256|"
    r"RELEASE-NOTES(?:_v[0-9.]+)?\.pdf|"
    r"Application-Notes_Cuvis-SDK(?:_[A-Za-z0-9-]+)?\.pdf|"
    r".+\.pdf|README\.md|RELEASE-NOTES\.md)$"
)

_PKG_ROLE = {
    "Cuvis_C_SDK_Installer": "installer",
    "libcuvis": "libcuvis",
    "cuviscommon": "cuviscommon",
}

# Module-level cache. Key = (include_prerelease, time-bucket); time-bucket =
# floor(now / cache_seconds). Bucketing means repeated calls within the window
# all hit the same key and skip the network.
_cache: dict[tuple[bool, int], list[dict[str, Any]]] = {}


def _fetch_all_releases(
    include_prerelease: bool, cache_seconds: int
) -> list[dict[str, Any]]:
    bucket = int(time.time() // max(cache_seconds, 1))
    key = (include_prerelease, bucket)
    if key in _cache:
        return _cache[key]
    req = urllib.request.Request(
        RELEASES_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "cuvis-sdk-url",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if not include_prerelease:
        data = [r for r in data if not r.get("prerelease")]
    _cache.clear()
    _cache[key] = data
    return data


def _resolve_release(
    version: str | None,
    include_prerelease: bool,
    cache_seconds: int,
) -> dict[str, Any]:
    releases = _fetch_all_releases(include_prerelease, cache_seconds)
    if not releases:
        raise LookupError(f"No releases found on {REPO}")
    if version is None:
        return releases[0]
    for r in releases:
        if r.get("tag_name") == version:
            return r
    raise LookupError(f"Release '{version}' not found on {REPO}")


def _matching_pattern_a(
    release: dict[str, Any],
    os: str,
    arch: str,
    cuda: str,
) -> dict[str, dict[str, str]]:
    """Group Pattern-A assets by package role for the given (os, arch, cuda)."""
    out: dict[str, dict[str, str]] = {}
    for asset in release.get("assets", []):
        name = asset.get("name", "")
        m = REGEX_INSTALLER.match(name)
        if not m:
            continue
        if (
            m.group("os") != os
            or m.group("arch") != arch
            or m.group("cuda") != cuda
        ):
            continue
        role = _PKG_ROLE[m.group("pkg")]
        out[role] = {
            "name": name,
            "url": asset.get("browser_download_url", ""),
        }
    return out


def sdk_urls(
    os: str,
    arch: str = "amd64",
    cuda: str = "nocuda",
    *,
    version: str | None = None,
    include_prerelease: bool = False,
    cache_seconds: int = 1800,
) -> dict[str, str]:
    """Resolve all release-asset browser_download_urls for the given target.

    Returns a {role: url} dict. Roles:
      - "installer"   — Windows (.exe), macOS (.dmg/.pkg), single-file installers.
      - "libcuvis"    — Ubuntu .deb pair; the binary library.
      - "cuviscommon" — Ubuntu .deb pair; common files (install before libcuvis).

    Raises LookupError if no matching asset exists on the release.
    """
    release = _resolve_release(version, include_prerelease, cache_seconds)
    matches = _matching_pattern_a(release, os, arch, cuda)
    if not matches:
        raise LookupError(
            f"No installer/package assets on {release.get('tag_name')} "
            f"for os={os!r} arch={arch!r} cuda={cuda!r}"
        )
    return {role: m["url"] for role, m in matches.items()}


def sdk_url(
    os: str,
    arch: str = "amd64",
    cuda: str = "nocuda",
    *,
    version: str | None = None,
    include_prerelease: bool = False,
    package: str = "installer",
    cache_seconds: int = 1800,
) -> str:
    """Single-asset variant of `sdk_urls`.

    `package` is the role name from `sdk_urls` — "installer" (Windows/macOS),
    "libcuvis" or "cuviscommon" (Ubuntu).

    Raises LookupError if no asset matches that role on that target.
    """
    urls = sdk_urls(
        os=os,
        arch=arch,
        cuda=cuda,
        version=version,
        include_prerelease=include_prerelease,
        cache_seconds=cache_seconds,
    )
    if package not in urls:
        raise LookupError(
            f"No '{package}' asset for os={os!r} arch={arch!r} cuda={cuda!r}; "
            f"available roles: {sorted(urls)}"
        )
    return urls[package]


def install_command(
    os: str,
    arch: str = "amd64",
    cuda: str = "nocuda",
    *,
    version: str | None = None,
    include_prerelease: bool = False,
    cache_seconds: int = 1800,
) -> str:
    """Returns a copy-pasteable shell command for the given target.

    - **Windows:** `Invoke-WebRequest` line + a launch line.
    - **macOS:**   `curl -O` line + an "open the disk image" hint.
    - **Ubuntu:**  three lines — two `curl -O` calls (cuviscommon then libcuvis),
      followed by `sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb`. Order
      matters: libcuvis depends on cuviscommon.
    """
    urls = sdk_urls(
        os=os,
        arch=arch,
        cuda=cuda,
        version=version,
        include_prerelease=include_prerelease,
        cache_seconds=cache_seconds,
    )

    if os.startswith("Ubuntu"):
        lib = urls.get("libcuvis")
        common = urls.get("cuviscommon")
        if not (lib and common):
            raise LookupError(
                f"Ubuntu target {os}/{arch}/{cuda} missing libcuvis or cuviscommon"
            )
        return (
            f"curl -O {common}\n"
            f"curl -O {lib}\n"
            f"sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb"
        )

    if "installer" not in urls:
        raise LookupError(f"No 'installer' asset for {os}/{arch}/{cuda}")
    installer_url = urls["installer"]
    name = installer_url.rsplit("/", 1)[-1]

    if os == "Windows":
        return (
            f"Invoke-WebRequest -Uri {installer_url} -OutFile {name}\n"
            f"Start-Process -Wait -FilePath .\\{name}"
        )

    if os == "macOS":
        return (
            f"curl -O {installer_url}\n"
            f"# Open {name} and follow the installer prompts"
        )

    raise LookupError(f"Unsupported os '{os}' for install_command")


def list_release_metadata(
    version: str | None = None,
    *,
    include_prerelease: bool = False,
    cache_seconds: int = 1800,
) -> dict[str, str]:
    """Returns Pattern-B asset names mapped to download URLs for the release.

    Used by the docs site selector to render named "Release notes (PDF)" /
    "Application notes (PDF)" / "Checksums" links beneath the install command.
    Excludes Pattern-A binaries even though some of them (like .deb) might be
    permissive matches of the broad `.+\\.pdf` alternative — we only return
    files that match Pattern B and *don't* match Pattern A.
    """
    release = _resolve_release(version, include_prerelease, cache_seconds)
    out: dict[str, str] = {}
    for asset in release.get("assets", []):
        name = asset.get("name", "")
        if REGEX_METADATA.match(name) and not REGEX_INSTALLER.match(name):
            out[name] = asset.get("browser_download_url", "")
    return out


# --- CLI ---------------------------------------------------------------------


def _add_target_args(sp: argparse.ArgumentParser, *, with_package: bool = False) -> None:
    sp.add_argument(
        "--os",
        required=True,
        help="OS token: Windows | macOS | Ubuntu24.04 | Ubuntu22.04-jetson-experimental | …",
    )
    sp.add_argument("--arch", default="amd64", help="amd64 | arm64 (default: amd64)")
    sp.add_argument(
        "--cuda",
        default="nocuda",
        help="nocuda | cuda12.3 | cuda13.0 | … (default: nocuda)",
    )
    sp.add_argument(
        "--version",
        default=None,
        help="Release tag, e.g. v3.5.3 (default: latest non-prerelease)",
    )
    sp.add_argument(
        "--include-prerelease",
        action="store_true",
        help="Include prerelease releases when resolving --version",
    )
    if with_package:
        sp.add_argument(
            "--package",
            default="installer",
            choices=["installer", "libcuvis", "cuviscommon"],
            help="Asset role (default: installer)",
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="cuvis_sdk_url",
        description="Resolve Cuvis SDK release-asset URLs from GitHub Releases.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    _add_target_args(sub.add_parser("url", help="Print one asset URL"), with_package=True)
    _add_target_args(sub.add_parser("urls", help="Print JSON dict of role → URL"))
    _add_target_args(
        sub.add_parser("install-command", help="Print copy-pasteable install command")
    )

    p_meta = sub.add_parser(
        "metadata", help="Print JSON dict of name → URL for Pattern-B release metadata"
    )
    p_meta.add_argument(
        "--version",
        default=None,
        help="Release tag, e.g. v3.5.3 (default: latest non-prerelease)",
    )
    p_meta.add_argument(
        "--include-prerelease",
        action="store_true",
        help="Include prerelease releases when resolving --version",
    )

    args = parser.parse_args(argv)

    try:
        if args.cmd == "metadata":
            print(
                json.dumps(
                    list_release_metadata(
                        version=args.version,
                        include_prerelease=args.include_prerelease,
                    ),
                    indent=2,
                )
            )
            return 0

        target_kwargs = dict(
            os=args.os,
            arch=args.arch,
            cuda=args.cuda,
            version=args.version,
            include_prerelease=args.include_prerelease,
        )
        if args.cmd == "url":
            print(sdk_url(package=args.package, **target_kwargs))
        elif args.cmd == "urls":
            print(json.dumps(sdk_urls(**target_kwargs), indent=2))
        elif args.cmd == "install-command":
            print(install_command(**target_kwargs))
    except LookupError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
