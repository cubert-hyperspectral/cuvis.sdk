#!/usr/bin/env python3
"""Stage the SDK share tree into GitHub Release asset names, or lint a release's asset list.

    python scripts/release_assets.py stage --version 3.6.0 --source _assets --dest _assets/.staging/v3.6.0
    python scripts/release_assets.py lint --tag v3.6.0
    python scripts/release_assets.py lint --path _assets/.staging/v3.6.0

The naming grammar lives in scripts/asset_names.py and is shared with the docs selector.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from asset_names import barren, recognised, staged, unparsed

REPO = "cubert-hyperspectral/cuvis.sdk"
CHUNK = 1 << 20


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stage(source: Path, destination: Path, version: str, strict: bool = False) -> dict[Path, str]:
    if skipped := unparsed(source):
        sys.exit("share folders the naming grammar does not recognise:\n  " + "\n  ".join(skipped))

    # A variant whose build job produced nothing leaves an empty folder behind. The old
    # PowerShell staged around it silently and the release shipped a variant short.
    if empty := barren(source):
        report = "variant folders holding no package:\n  " + "\n  ".join(empty)
        if strict:
            sys.exit(report)
        print(f"::warning title=incomplete share::{report}", file=sys.stderr)

    plan = staged(source, version)
    if not plan:
        sys.exit(f"{source} holds nothing publishable")

    destination.mkdir(parents=True, exist_ok=True)
    for origin, name in plan.items():
        shutil.copy2(origin, destination / name)

    names = sorted(plan.values())
    (destination / "SHA256SUMS.txt").write_text(
        "".join(f"{sha256(destination / name)}  {name}\n" for name in names), encoding="ascii"
    )
    return plan


def published(tag: str, repo: str) -> list[str]:
    view = subprocess.run(
        ["gh", "release", "view", tag, "--repo", repo, "--json", "assets"],
        capture_output=True, text=True, check=True,
    )
    return [asset["name"] for asset in json.loads(view.stdout)["assets"]]


def lint(names: list[str]) -> int:
    rejected = [name for name in names if not recognised(name)]
    print("\n".join(f"  {'ok  ' if name not in rejected else 'FAIL'} {name}" for name in sorted(names)))
    if rejected:
        print(f"\n{len(rejected)} asset name(s) do not match the grammar in scripts/asset_names.py", file=sys.stderr)
    return 1 if rejected else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)

    staging = commands.add_parser("stage", help="rename one share tree into release asset names")
    staging.add_argument("--version", required=True, help="SDK version, e.g. 3.6.0")
    staging.add_argument("--source", type=Path, default=Path("_assets"), help="directory holding 'Cuvis <version>'")
    staging.add_argument("--dest", type=Path, help="staging directory (default _assets/.staging/v<version>)")
    staging.add_argument("--strict", action="store_true", help="fail instead of warn on a variant folder with no package")

    linting = commands.add_parser("lint", help="check asset names against the grammar")
    target = linting.add_mutually_exclusive_group(required=True)
    target.add_argument("--tag", help="lint the assets published on this release")
    target.add_argument("--path", type=Path, help="lint the file names in this directory")
    linting.add_argument("--repo", default=REPO)

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.command == "lint":
        names = published(args.tag, args.repo) if args.tag else [p.name for p in args.path.rglob("*") if p.is_file()]
        return lint(names)

    source = args.source / f"Cuvis {args.version}"
    destination = args.dest or Path("_assets/.staging") / f"v{args.version}"
    plan = stage(source, destination, args.version, args.strict)
    print("\n".join(f"  {origin.name}  ->  {name}" for origin, name in plan.items()))
    print(f"\n{len(plan)} assets staged in {destination}")
    return lint(sorted(plan.values()) + ["SHA256SUMS.txt"])


if __name__ == "__main__":
    raise SystemExit(main())
