# Reference: `cuvis_sdk_url` script

[`scripts/cuvis_sdk_url.py`](https://github.com/cubert-hyperspectral/cuvis.sdk/blob/main/scripts/cuvis_sdk_url.py)
is a single-file Python script that resolves Cuvis SDK release-asset URLs
from the live GitHub Releases API. It powers two things:

1. **The build-time macro** behind the `<noscript>` fallback on the
   [Installation](installation.md) page (the docs build imports it as a
   Python module via [`tools/docs_macros.py`](https://github.com/cubert-hyperspectral/cuvis.sdk/blob/main/tools/docs_macros.py)).
2. **A copy-pasteable CLI** for shell scripting, CI, and one-off lookups.

Pure stdlib, Python 3.10+, no install step. PEP 723 inline metadata makes it
`uv run`-friendly out of the box.

## CLI

Run from a clone of the repo:

```bash
uv run scripts/cuvis_sdk_url.py <subcommand> [options]
```

Four subcommands. All except `metadata` take `--os`, `--arch` (default
`amd64`), `--cuda` (default `nocuda`), `--version` (default: latest
non-prerelease), and `--include-prerelease`.

### `urls` — JSON dict of role → URL

```bash
uv run scripts/cuvis_sdk_url.py urls --os Ubuntu24.04
# {
#   "libcuvis":    "https://.../v3.5.3/libcuvis_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb",
#   "cuviscommon": "https://.../v3.5.3/cuviscommon_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb"
# }
```

### `url` — single asset URL (plain text)

```bash
uv run scripts/cuvis_sdk_url.py url --os Windows --cuda cuda12.3
# https://.../v3.5.3/Cuvis_C_SDK_Installer_3.5.3_Windows_amd64_cuda12.3.exe

uv run scripts/cuvis_sdk_url.py url \
    --os Ubuntu24.04 --package libcuvis
# https://.../v3.5.3/libcuvis_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb
```

`--package` is `installer` (default), `libcuvis`, or `cuviscommon`.

### `install-command` — copy-paste shell block

```bash
uv run scripts/cuvis_sdk_url.py install-command --os Ubuntu24.04
# curl -O https://.../cuviscommon_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb
# curl -O https://.../libcuvis_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb
# sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb
```

Two lines on Windows (`Invoke-WebRequest` + `Start-Process`), three on
Ubuntu (`curl`, `curl`, `sudo dpkg -i …`). Order matters on Linux:
`cuviscommon` is installed before `libcuvis` because the latter depends
on the former.

### `metadata` — Pattern-B release artifacts

```bash
uv run scripts/cuvis_sdk_url.py metadata --version v3.5.1
# {
#   "RELEASE-NOTES_v3.5.1.pdf":          "https://.../RELEASE-NOTES_v3.5.1.pdf",
#   "Application-Notes_Cuvis-SDK_Linux.pdf": "https://.../Application-Notes_Cuvis-SDK_Linux.pdf",
#   "SHA256SUMS.txt":                    "https://.../SHA256SUMS.txt"
# }
```

Returns release-notes PDFs, application-notes PDFs, and `SHA256SUMS.txt`.
Pattern-A binaries (Pattern-A is the installer/package naming grammar)
are explicitly excluded.

## Pinning a specific version

Pass `--version v3.5.0` (or any other tag from
[the releases page](https://github.com/cubert-hyperspectral/cuvis.sdk/releases))
to any subcommand. Without `--version`, the script picks the latest
non-prerelease release.

## Token reference

The values you pass to `--os`, `--arch`, `--cuda` must match the asset's
filename tokens exactly. They're enforced by the
[Pattern A regex](https://github.com/cubert-hyperspectral/cuvis.sdk/blob/main/scripts/lint-release-assets.ps1).

| Param | Allowed values |
| --- | --- |
| `--os` | `Windows`, `macOS`, `Ubuntu20.04`, `Ubuntu22.04`, `Ubuntu24.04`, `Ubuntu*-jetson-experimental` |
| `--arch` | `amd64`, `arm64` |
| `--cuda` | `nocuda`, `cuda11.8`, `cuda12.2`, `cuda12.3`, `cuda12.6`, `cuda13.0` |
| `--package` (only `url`) | `installer` (default), `libcuvis`, `cuviscommon` |
| `--version` | `None` = latest non-prerelease, or a tag like `v3.5.3` |

If no asset matches the combination, the script exits 1 with a `LookupError`
message on stderr.

## Used as a Python module from inside the repo

`tools/docs_macros.py` adds `scripts/` to `sys.path` and imports the
public functions to register them as mkdocs-macros for the `<noscript>`
fallback. Anyone working inside the repo can do the same:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path("/path/to/cuvis.sdk/scripts")))

from cuvis_sdk_url import sdk_url, sdk_urls, install_command
sdk_urls(os="Ubuntu24.04", cuda="cuda12.6")
```

External Python projects shouldn't depend on this — there's no PyPI
release. If you find yourself wanting one, you're better off writing a
thin wrapper around the
[GitHub Releases API](https://docs.github.com/en/rest/releases/releases)
directly.

## Caching

The script keeps a module-level cache keyed on `(include_prerelease,
time-bucket)` where `time-bucket = floor(now / cache_seconds)`. Default
TTL is 30 minutes. Repeated calls within a process re-use one fetched
payload. GitHub's unauthenticated REST API allows 60 requests/hour/IP, so
the cache keeps even tight loops well clear.
