#!/usr/bin/env bash
# Extracts cuvis.h from the SDK Docker image into docs/_api_sources/.
# Use this to set up the header for a partial local build (Doxygen C API only).
#
# Usage:
#   bash scripts/fetch-cuvis-header.sh
#   bash scripts/fetch-cuvis-header.sh cubertgmbh/cuvis_pyil:3.5.0-ubuntu24.04
#
# For a full local doc build (Python API requires live import of the SDK):
#   docker run --rm -v "$PWD:/workspace" -w /workspace \
#     cubertgmbh/cuvis_pyil:3.5.0-ubuntu24.04 \
#     bash -c "apt-get update -y -q && apt-get install -y -q doxygen graphviz && \
#              mkdir -p docs/_api_sources && cp /usr/include/cuvis.h docs/_api_sources/ && \
#              pip install uv && uv sync --extra docs && uv run mkdocs build --strict"
set -euo pipefail

IMAGE="${1:-cubertgmbh/cuvis_pyil:3.5.0-ubuntu24.04}"
mkdir -p docs/_api_sources
cid=$(docker create "$IMAGE")
docker cp "${cid}:/usr/include/cuvis.h" docs/_api_sources/cuvis.h
docker rm "${cid}"
echo "cuvis.h extracted from ${IMAGE} → docs/_api_sources/cuvis.h"
