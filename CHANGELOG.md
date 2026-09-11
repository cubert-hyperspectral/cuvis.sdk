# Changelog

All notable changes to the cuvis SDK distribution hub are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Versions are `GENERATION.MAJOR.MINOR`, the cuvis SDK release whose installers this repository publishes.
Pre-releases (`a*`, `b*`, `rc*`) stage and lint the assets without creating a GitHub Release; their entries stay under `## [Unreleased]` until the final version.

## [Unreleased]

### Added

- `scripts/release_notes.py` - lifts the SDK's own release notes for the version out of `Release Notes.pdf` on the share and renders them as Markdown, restoring the spacing and the backticks around verbatim spans that the PDF's text layer drops.
- `CI` - the release body is now assembled from those notes followed by this repository's changelog section, instead of the changelog alone.
  A share with no release notes, or notes with no section for the version being released, fails the release.

## [3.6.0] - 2026-09-11

Publishes cuvis SDK 3.6.0.

### Added

- `CI` - `.github/workflows/release.yml` is driven by `v*` tags: it validates the tag against this file, downloads the SDK share for that version, stages and lints the assets, and creates a draft GitHub Release with the matching section here as notes.
  Nothing runs on a developer machine any more.
- `scripts/asset_names.py` - the naming grammar shared by the share folders, the release assets and the docs selector, with the os, arch, cuda and variant tokens left open so an SDK rename cannot fail a release.
- `scripts/release_assets.py` - stages one share tree into release asset names and lints an asset list, replacing the PowerShell tooling.
  It reports every unrecognised share folder at once rather than aborting on the first, and reports variant folders holding no package, which previously shipped as a silently missing platform.
- `docs` - the documentation site moved here from `cuvis.doc` and is published to GitHub Pages, versioned with `mike`: a `v*.*.*` tag publishes that version aliased to `latest`.
  C and C++ reference is generated from the headers with `mkdoxy`, the Python reference with `mkdocstrings`, the example pages from the Python notebooks, and an `llms.txt` / `llms-full.txt` index with `mkdocs-llmstxt`.
- `CI` - `.github/workflows/docs-check.yml` runs `mkdocs build --strict` on pull requests, and the deploy path builds strictly before `mike deploy`, so dead links or missing generated pages fail CI instead of publishing a broken site.

### Changed

- Submodules updated to their released state for SDK 3.6.0: `cuvis.c`, `cuvis.cpp`, `cuvis.csharp`, `cuvis.python` and the C, C++ and C# example repositories.
  `cuvis.python` moves to 3.6.0.0, whose `cuvis-il` requirement is `>=3.6.0,<3.7.0`.
- `cudano` and `nocuda` are both accepted as the CUDA-less token, because the SDK share renamed it in 3.6.0.
  Published asset names keep `nocuda`, so one selector resolves every release back to v3.2.
- Jetson folders lost their `-experimental` suffix in 3.6.0. Both spellings parse, and the suffix is carried into the asset name instead of being matched against a fixed list.
- Platform coverage follows SDK 3.6.0: Ubuntu 20.04 is gone, Ubuntu 26.04 is new.
- `CI` - the docs workflows build in `cubertgmbh/cuvis_pyil:3.6.0-ubuntu24.04`, which supplies the `cuvis.h` the Doxygen reference is generated from.
- `CI` - the docs deploys share a `docs-deploy` concurrency group so a `main` push and a release tag cannot race each other's push to `gh-pages`.
- `mkdocs.yml` - the site follows Cubert branding: the Material palette is driven from `docs/stylesheets/extra.css` across both schemes, headings use Rajdhani, body and code stay on Roboto and Roboto Mono, and the existing `.sdk-installer` styles sit on top of it.
- `llms.txt` - the generated index covers the guide and the Python API and now includes the home page; the generated mkdoxy pages are left out so the strict build has no plugin-order dependency.

### Removed

- `scripts/fetch-installers.ps1` - the share is one public zip per version, the same one cuvis.docker and cuvis.pyil download, so mirroring it over WebDAV with a hardcoded share token was 181 lines solving a problem that does not exist.
- `scripts/stage-release-assets.ps1`, `scripts/lint-release-assets.ps1` - replaced by `scripts/release_assets.py`.
- `CI` - the nightly `deploy-docs.yml` and its `/dev/` channel; the site updates only on release tags, and the stale `dev` version was deleted from `gh-pages`.

### Fixed

- `CI` - the docs deploy could never push to `gh-pages` from inside the build container, because git rejected the container-checked-out workspace with `fatal: not in a git directory`. The workspace is marked safe after checkout.
- `tools/example_pages.py` - `_parse_notebook` dropped the closing text of a notebook ending in a markdown cell, because it flushed the final section only on leftover code.
- `docs/examples/index.md` - the overview promised per-example C and C++ tabs the generator never produced; the example pages are Python only, and the C and C++ sources live in the `examples/` submodules.
- `mkdocs.yml` - `content.code.annotation` was a typo for `content.code.annotate`, so code annotations did not render.
