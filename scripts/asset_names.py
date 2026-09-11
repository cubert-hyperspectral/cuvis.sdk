#!/usr/bin/env python3
"""The naming grammar shared by the SDK share, the release assets and the docs selector.

A share folder is `<os>[ <osver>-]<arch>-<cuda>[-<variant>]`, a source package is
`<pkg>_<pkgver>.<ext>`, and a release asset is `<pkg>_<pkgver>_<os>[-<variant>]_<arch>_<cuda>.<ext>`.

The os, arch, cuda and variant tokens are open patterns on purpose. The SDK renames them
between releases - 3.6.0 turned `nocuda` into `cudano` and dropped `-experimental` from the
Jetson folders - and a closed alternation turns every such rename into a failed release.
"""

from __future__ import annotations

import re
from pathlib import Path

FOLDER = re.compile(
    r"(?P<os>[A-Za-z]+) (?:(?P<osver>[0-9.]+)-)?"
    r"(?P<arch>[^-]+)-(?P<cuda>[^-]+)(?:-(?P<variant>.+))?"
)

SOURCE = re.compile(
    r"(?P<pkg>.+)_(?P<pkgver>[0-9][0-9.]*(?:-[0-9]+)?)"
    r"\.(?P<ext>exe|deb|msi|dmg|pkg|tar\.gz)"
)

ASSET = re.compile(
    r"(?P<pkg>.+)_(?P<pkgver>[0-9][0-9.]*(?:-[0-9]+)?)"
    r"_(?P<os>[^_]+)_(?P<arch>[^_]+)_(?P<cuda>[^_]+)"
    r"\.(?P<ext>exe|deb|msi|dmg|pkg|tar\.gz)"
)

METADATA = re.compile(
    r"SHA256SUMS\.txt|.+\.sha256"
    r"|RELEASE-NOTES(?:_v[0-9.]+)?\.(?:pdf|md)"
    r"|Application-Notes_Cuvis-SDK(?:_[A-Za-z0-9-]+)?\.pdf"
    r"|.+\.pdf|README\.md"
)

# Published names keep the older spelling of the CUDA-less token so one selector resolves
# every release back to v3.2; both spellings parse. A future rename is one entry.
CUDA_SYNONYMS = {"cudano": "nocuda"}

PDF_RENAMES = (
    (re.compile(r"Release Notes\.pdf"), "RELEASE-NOTES_v{version}.pdf"),
    (re.compile(r"Application_Notes_Cuvis_SDK_(?P<topic>.+)\.pdf"), "Application-Notes_Cuvis-SDK_{topic}.pdf"),
)


def os_token(folder: re.Match[str]) -> str:
    return "".join(filter(None, (folder["os"], folder["osver"], f"-{folder['variant']}" if folder["variant"] else "")))


def asset_name(folder: re.Match[str], source: re.Match[str]) -> str:
    cuda = CUDA_SYNONYMS.get(folder["cuda"], folder["cuda"])
    return f"{source['pkg']}_{source['pkgver']}_{os_token(folder)}_{folder['arch']}_{cuda}.{source['ext']}"


def metadata_name(name: str, version: str) -> str | None:
    """The published name of a top-level document, or None when it is not one."""
    return next(
        (
            template.format(version=version, **match.groupdict())
            for pattern, template in PDF_RENAMES
            if (match := pattern.fullmatch(name))
        ),
        None,
    )


def staged(root: Path, version: str) -> dict[Path, str]:
    """Every file under one `Cuvis <version>` tree mapped to the name it is published under."""
    packages = {
        source: asset_name(folder, match)
        for directory in sorted(root.iterdir())
        if directory.is_dir() and (folder := FOLDER.fullmatch(directory.name))
        for source in sorted(directory.iterdir())
        if (match := SOURCE.fullmatch(source.name))
    }
    documents = {
        document: name
        for document in sorted(root.iterdir())
        if document.is_file() and (name := metadata_name(document.name, version))
    }
    return packages | documents


def unparsed(root: Path) -> list[str]:
    """Directory names the folder grammar does not recognise, which would be published as nothing."""
    return [d.name for d in sorted(root.iterdir()) if d.is_dir() and not FOLDER.fullmatch(d.name)]


def barren(root: Path) -> list[str]:
    """Variant folders that parse but hold no package, so the share was built from an incomplete pipeline."""
    return [
        d.name
        for d in sorted(root.iterdir())
        if d.is_dir() and FOLDER.fullmatch(d.name)
        and not any(SOURCE.fullmatch(f.name) for f in d.iterdir())
    ]


def recognised(name: str) -> bool:
    return bool(ASSET.fullmatch(name) or METADATA.fullmatch(name))
