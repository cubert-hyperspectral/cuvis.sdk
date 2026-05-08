# Cuvis SDK

The Cuvis SDK is the C/C++ library and language wrappers that power Cubert
hyperspectral cameras. This site is the canonical entry point for installing
the SDK and finding the language binding that fits your project.

## Get started

- **[Install the SDK](installation.md)** — pick your OS, CPU architecture, and
  CUDA stack from the selector. Works for Windows, Ubuntu 20.04 / 22.04 /
  24.04 (amd64 and Jetson arm64), and macOS.
- **All releases:** [github.com/cubert-hyperspectral/cuvis.sdk/releases](https://github.com/cubert-hyperspectral/cuvis.sdk/releases) — every
  installer, every version, every platform. The selector page is just a
  filter on top of these.

## Language wrappers

Each wrapper lives in a top-level submodule of
[`cuvis.sdk`](https://github.com/cubert-hyperspectral/cuvis.sdk):

- **C** — [`cuvis.c`](https://github.com/cubert-hyperspectral/cuvis.c)
- **C++** — [`cuvis.cpp`](https://github.com/cubert-hyperspectral/cuvis.cpp)
- **C#** — [`cuvis.csharp`](https://github.com/cubert-hyperspectral/cuvis.csharp)
- **Python** — [`cuvis.python`](https://github.com/cubert-hyperspectral/cuvis.python)

The example code for each lives in `examples/<language>/` in the umbrella
repo. Sample measurements (no camera required) are described in
[`sample_data/`](https://github.com/cubert-hyperspectral/cuvis.sdk/tree/main/sample_data).

## Need help?

- **Code-related issues:** open one on
  [GitHub](https://github.com/cubert-hyperspectral/cuvis.sdk/issues).
- **Application support:** [Cubert support portal](http://support.cubert-hyperspectral.com/).
- **Cubert website:** [cubert-hyperspectral.com](https://www.cubert-hyperspectral.com/).
