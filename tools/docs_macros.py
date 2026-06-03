"""mkdocs-macros entrypoint for the Cuvis SDK docs site.

Registers the `cuvis_sdk_url` helper as a set of mkdocs-macros so that
`installation.md` can call e.g. `{{ cuvis_install_command(os="Ubuntu24.04") }}`
and get a baked-in shell command at build time. The result is used as the
noscript fallback under the JS selector form.

The helper lives at `scripts/cuvis_sdk_url.py` (no longer an installable
package); we add `scripts/` to `sys.path` so the import below resolves.
Edits to the script are visible in the next `uv run mkdocs build` with no
intermediate install step.

Also registers `multilang_example(name)` which generates the multi-language
tabbed example pages from the Jupyter notebooks and C/C++ source files in
``examples/``. Implementation is in ``tools/example_pages.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
_SCRIPTS_DIR = _TOOLS_DIR.parent / "scripts"
for _p in (_TOOLS_DIR, _SCRIPTS_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


def define_env(env):
    from cuvis_sdk_url import (
        REPO,
        install_command,
        list_release_metadata,
        sdk_url,
        sdk_urls,
    )
    from example_pages import multilang_example

    def _safe_install_command(*args, **kwargs):
        try:
            return install_command(*args, **kwargs)
        except Exception as exc:
            return (
                f"# Couldn't resolve install command at build time ({exc!s}).\n"
                f"# Browse all releases at https://github.com/{REPO}/releases"
            )

    env.macro(sdk_url, "cuvis_sdk_url")
    env.macro(sdk_urls, "cuvis_sdk_urls")
    env.macro(_safe_install_command, "cuvis_install_command")
    env.macro(list_release_metadata, "cuvis_sdk_metadata")
    env.macro(multilang_example)
