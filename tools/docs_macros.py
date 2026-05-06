"""mkdocs-macros entrypoint for the Cuvis SDK docs site.

Registers the `cuvis_sdk_url` helper as a set of mkdocs-macros so that
`installation.md` can call e.g. `{{ cuvis_install_command(os="Ubuntu24.04") }}`
and get a baked-in shell command at build time. The result is used as the
noscript fallback under the JS selector form.

The helper is editable-installed via `[tool.uv.sources]` in the root
`pyproject.toml`, so any edit to `python/cuvis_sdk_url.py` is visible in the
next `uv run mkdocs build` without re-running `uv sync`.
"""

from __future__ import annotations


def define_env(env):
    from cuvis_sdk_url import (
        REPO,
        install_command,
        list_release_metadata,
        sdk_url,
        sdk_urls,
    )

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
