# Releasing

How to publish a new Cuvis C SDK version on GitHub Releases.

## Prerequisites

- Installers downloaded into `_assets/Cuvis <ver>/...` (use `scripts/fetch-installers.ps1`).
- `gh` CLI authenticated against `cubert-hyperspectral/cuvis.sdk` with `repo` scope.
- PowerShell 7+ (`pwsh`).

## Publish a new version (e.g. v3.5.3)

```powershell
git tag v3.5.3
git push origin v3.5.3
gh release create v3.5.3 --draft --notes-file release-notes/v3.5.3.md
pwsh scripts/stage-release-assets.ps1 -Version 3.5.3 -Upload
gh release edit v3.5.3 --draft=false
```

## Add assets to an existing empty release (e.g. v3.4.1)

If the tag/release already exists but has no assets attached, skip the tag/create
steps and only stage + upload:

```powershell
pwsh scripts/stage-release-assets.ps1 -Version 3.4.1 -Upload
```

The release stays published; only its asset list changes.

## What `stage-release-assets.ps1` does

1. Reads `_assets/Cuvis <ver>/` (downloaded by `fetch-installers.ps1`).
2. Parses each parent directory like
   `Ubuntu 22.04-arm64-cuda13.0-jetson-experimental` into `(os, arch, cuda)`
   tokens.
3. Renames binaries to the canonical flat scheme:
   `<pkg>_<pkgver>_<os>_<arch>_<cuda>.<ext>`.
4. Renames PDFs:
   - `Release Notes.pdf` → `RELEASE-NOTES_v<ver>.pdf`
   - `Application_Notes_Cuvis_SDK_<topic>.pdf` →
     `Application-Notes_Cuvis-SDK_<topic>.pdf`
5. Computes SHA-256 for every binary and PDF and writes an aggregate
   `SHA256SUMS.txt`. (No per-file `.sha256` sidecars — they doubled the
   asset count for no real benefit; users can `grep <name> SHA256SUMS.txt`
   or read the GitHub API's per-asset `digest` field.)
6. Runs `scripts/lint-release-assets.ps1` against the staged file set; aborts
   on the first mismatch.
7. With `-Upload`: uploads everything to the matching `v<ver>` release via
   `gh release upload --clobber`.

Staging happens under `_assets/.staging/v<ver>/` (gitignored).

## CI guard

`.github/workflows/release-asset-lint.yml` runs the same lint script on every
`release: published` and `release: edited` event, plus on-demand via
`workflow_dispatch` (with a `tag` input). Every uploaded asset must match
either:

- **Pattern A** (installers/packages): `<pkg>_<pkgver>_<os>_<arch>_<cuda>.<ext>`
- **Pattern B** (release metadata): `SHA256SUMS.txt`, `<asset>.sha256`,
  `RELEASE-NOTES*.pdf`, `Application-Notes_Cuvis-SDK*.pdf`, etc.

See `scripts/lint-release-assets.ps1` for the canonical regexes — the same
patterns are also exported by `python/cuvis_sdk_url.py` and used by the
in-repo docs site selector (`docs/javascripts/sdk-installer.js`).

## Token grammar

| Token | Examples | Notes |
| --- | --- | --- |
| `<pkg>` | `Cuvis_C_SDK_Installer`, `libcuvis`, `cuviscommon` | Selector treats `libcuvis` + `cuviscommon` as a Linux pair on Ubuntu. |
| `<pkgver>` | `3.5.3`, `3.5.3-0`, `3.4.1-1` | Carries the upstream installer's debian-revision verbatim. Selector groups by **release tag**, not `<pkgver>`. |
| `<os>` | `Windows`, `Ubuntu24.04`, `Ubuntu22.04-jetson`, `Ubuntu22.04-jetson-experimental` | Jetson is an OS flavor. Promote `*-jetson-experimental` → `*-jetson` when stable. |
| `<arch>` | `amd64`, `arm64` | Clean ISA enum. Jetson lives in `<os>`, not here. |
| `<cuda>` | `nocuda`, `cuda11.8`, `cuda12.2`, `cuda12.3`, `cuda12.6`, `cuda13.0` | Extend as needed; the lint regex permits any `cuda<digits>.<digits>`. |
| `<ext>` | `exe`, `deb`, `msi`, `dmg`, `pkg`, `tar.gz` | |

## Why one regex, three places?

- **Lint script** (this directory) — the source of truth; every release CI run
  shells out to it.
- **`scripts/cuvis_sdk_url.py`** — `REGEX_INSTALLER` / `REGEX_METADATA`;
  consumed at build time by the docs macros (via a `sys.path` injection in
  `tools/docs_macros.py`) and as a CLI for shell-side URL resolution
  (`uv run scripts/cuvis_sdk_url.py …`).
- **`docs/javascripts/sdk-installer.js`** — same Pattern A / B for client-side
  parsing of the GitHub Releases API.

If you change one, update the other two and bump the docs site cache key.
