# Releasing

How to publish a new Cuvis C SDK version on GitHub Releases.

A release is a `v<version>` tag on `main`. Everything after that is `.github/workflows/release.yml`.
Nothing runs on a developer machine, and no PowerShell or Nextcloud credential is involved.

## Prerequisites

- The SDK share for the version is published on `cloud.cubert-gmbh.de`, and its share token is named
  `cuvis_sdk_release_ver_<version without dots>`. For 3.6.0 that is `cuvis_sdk_release_ver_360`.
  The workflow builds that URL from the tag; a share under any other name fails the run at its first step.
  cuvis.docker and cuvis.pyil read the same share, so it is usually already correct by the time this repository releases.
- The submodules on `main` point at the wrapper releases for this SDK.
- `CHANGELOG.md` has a `## [<version>] - <date>` section and an empty `## [Unreleased]` above it.
- The share carries `Release Notes.pdf` and it has a section for this version. The release fails without it.

## Publish a new version

```bash
git checkout main && git pull
git tag -a v3.6.0 -m "Cuvis SDK 3.6.0"
git push origin v3.6.0
```

The workflow then validates the tag against `CHANGELOG.md` and confirms it is on `main`, downloads the
share zip for that version, stages the installers into the flat asset names, lints them, and opens a
**draft** Release whose body is assembled as described below.

Check the asset list, then publish the Release. `release-asset-lint.yml` lints it again on publish.

## Release notes

The body is assembled, not written: the SDK's own notes for this version first, then a
"cuvis.sdk repo Changes" heading, then this repository's changelog section.

`scripts/release_notes.py` lifts the SDK half out of `Release Notes.pdf` on the share, which is the
same file published as the `RELEASE-NOTES_v<version>.pdf` asset. The PDF is cumulative, so only the
section for the version being released is taken; a version it does not cover fails the release, as
does a share with no notes at all.

Two properties of that PDF's text layer are worth knowing, because they look like bugs in the output
and are not:

- LaTeX emits no space around a verbatim span, so `the use_compressed_lut settings` arrives as one
  word. The spans carry their own typewriter font, which is how the spacing is restored and how they
  end up fenced in backticks.
- Paragraphs are hard-wrapped with hyphenation, so `pro-` and `cessing` arrive on separate lines and
  are rejoined.

Anything the notes render as prose rather than verbatim stays prose. The Release is a draft, so
copy-edit it there if a term wants backticks the PDF did not mark up.

To see what the body will be without tagging:

```bash
python scripts/release_notes.py --version X.Y.Z --source _assets
```

## Dry-running a share

A pre-release tag stages and lints without creating a Release, which is the cheapest way to check a share
that was just uploaded:

```bash
git tag -a v3.6.0rc1 -m "dry run" && git push origin v3.6.0rc1
```

A final release also fails when a variant folder holds no package, which is how a build job that produced
nothing stops being a silently missing platform. A pre-release only warns.

To check a local tree instead:

```bash
python scripts/release_assets.py stage --version 3.6.0 --source _assets
python scripts/release_assets.py lint --path _assets/.staging/v3.6.0
```

## What the staging does

1. Reads `_assets/Cuvis <version>/`, one directory per variant.
2. Parses each directory name into `(os, osver, arch, cuda, variant)`.
3. Renames the packages to `<pkg>_<pkgver>_<os>[-<variant>]_<arch>_<cuda>.<ext>`.
4. Renames the documents: `Release Notes.pdf` to `RELEASE-NOTES_v<version>.pdf`, and
   `Application_Notes_Cuvis_SDK_<topic>.pdf` to `Application-Notes_Cuvis-SDK_<topic>.pdf`.
5. Writes one aggregate `SHA256SUMS.txt`. There are no per-file `.sha256` sidecars; they doubled the asset
   count for no benefit, and the GitHub API exposes a per-asset `digest` anyway.
6. Lints the staged names and fails before anything is uploaded.

## Token grammar

| Token | Examples | Notes |
| --- | --- | --- |
| `<pkg>` | `Cuvis_C_SDK_Installer`, `libcuvis`, `cuviscommon` | The selector treats `libcuvis` and `cuviscommon` as a Linux pair on Ubuntu. |
| `<pkgver>` | `3.6.0`, `3.6.0-0` | Carries the upstream installer's debian revision verbatim. The selector groups by release tag, not by `<pkgver>`. |
| `<os>` | `Windows`, `Ubuntu24.04`, `Ubuntu24.04-jetson` | Jetson is an OS flavour, not an architecture. The suffix is whatever the share folder carries, so `-jetson-experimental` still works. |
| `<arch>` | `amd64`, `arm64` | |
| `<cuda>` | `nocuda`, `cuda12.2`, `cuda12.9`, `cuda13.3` | The share spells the CUDA-less build `cudano` since 3.6.0. Both spellings parse; published names keep `nocuda` so one selector resolves every release back to v3.2. |
| `<ext>` | `exe`, `deb`, `msi`, `dmg`, `pkg`, `tar.gz` | |

The os, arch, cuda and variant tokens are open patterns rather than fixed lists.
The SDK renames them between releases, and a closed list turns every rename into a failed release, which is
exactly what `cudano` did in 3.6.0.

## Where the grammar lives

- **`scripts/asset_names.py`** is the source of truth. `scripts/release_assets.py` and
  `scripts/cuvis_sdk_url.py` both import it, so staging, linting, the CLI and the docs macros cannot disagree.
- **`docs/javascripts/sdk-installer.js`** keeps its own copy, because it parses the GitHub Releases API in the
  browser. `scripts/tests/test_asset_names.py` asserts that copy still accepts every name the stager produces,
  so it cannot drift silently. If you change it, bump the docs site cache key.
