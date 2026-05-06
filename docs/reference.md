# Reference: `cuvis_sdk_url` Python helper

`cuvis_sdk_url` is the same Python module that powers the build-time macros
on this site and the runtime URL resolution for downstream tools. It's a
pure-stdlib helper — no third-party dependencies.

Source:
[`python/cuvis_sdk_url.py`](https://github.com/cubert-hyperspectral/cuvis.sdk/blob/main/python/cuvis_sdk_url.py).

## Install

```bash
# From a clone of cubert-hyperspectral/cuvis.sdk:
uv pip install -e ./python

# Or directly from a checkout via path:
pip install -e <path-to-cuvis.sdk>/python
```

Requires Python 3.10+.

## Public API

### `sdk_urls(os, arch="amd64", cuda="nocuda", *, version=None, include_prerelease=False) -> dict[str, str]`

Resolve all release-asset URLs for a given target. Returns a `{role: url}` dict.
Roles are:

- `"installer"` — Windows `.exe`, macOS `.dmg`/`.pkg`, single-file installers.
- `"libcuvis"`, `"cuviscommon"` — Ubuntu `.deb` pair. Install order matters:
  cuviscommon first.

Raises `LookupError` if no asset matches.

```python
from cuvis_sdk_url import sdk_urls

# Latest non-prerelease, Ubuntu 24.04 amd64 no-CUDA:
sdk_urls(os="Ubuntu24.04")
# {'libcuvis': 'https://github.com/.../libcuvis_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb',
#  'cuviscommon': 'https://github.com/.../cuviscommon_3.5.3-0_Ubuntu24.04_amd64_nocuda.deb'}
```

### `sdk_url(os, arch="amd64", cuda="nocuda", *, version=None, include_prerelease=False, package="installer") -> str`

Single-asset variant. `package` is the role name from `sdk_urls`.

### `install_command(os, arch="amd64", cuda="nocuda", *, version=None, include_prerelease=False) -> str`

Returns a copy-pasteable shell command. Three lines for Ubuntu (curl, curl,
`sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb`), two for Windows
(`Invoke-WebRequest` + `Start-Process`), two for macOS.

### `list_release_metadata(version=None, *, include_prerelease=False) -> dict[str, str]`

Returns Pattern-B asset names mapped to download URLs (release-notes PDFs,
SHA256SUMS.txt, application-notes, etc.) for the chosen release.

## Exported regexes

`REGEX_INSTALLER` (Pattern A — installers and packages) and `REGEX_METADATA`
(Pattern B — release metadata). Identical to the patterns enforced by
[`scripts/lint-release-assets.ps1`](https://github.com/cubert-hyperspectral/cuvis.sdk/blob/main/scripts/lint-release-assets.ps1)
and the JS selector on the [Installation](installation.md) page.

## Caching

`sdk_urls`/`sdk_url`/etc. share a module-level cache keyed on
`(include_prerelease, time-bucket)` where `time-bucket = floor(now /
cache_seconds)`. By default `cache_seconds=1800` (30 minutes), so repeated
calls in a process re-use one fetched payload. Pass `cache_seconds=0` to
disable.

GitHub's unauthenticated REST API allows 60 requests/hour/IP. If you're
calling the helper in a tight loop, the cache keeps you well under that
limit.
