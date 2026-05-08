# Install Cuvis SDK

Pick your platform — the selector below queries
[GitHub Releases](https://github.com/cubert-hyperspectral/cuvis.sdk/releases)
live and emits the right download command for your OS, CPU architecture, and
CUDA stack.

<form id="cuvis-sdk-installer" class="sdk-installer">
  <p class="sdk-installer__loading">Loading installer selector…</p>
</form>

<noscript>
JavaScript is disabled, so the selector can't run. The default install command
for **Ubuntu 24.04 / amd64 / no CUDA** (built into the page at deploy time):

```bash
{{ cuvis_install_command(os="Ubuntu24.04", arch="amd64", cuda="nocuda") }}
```

For other platforms, browse
[all releases](https://github.com/cubert-hyperspectral/cuvis.sdk/releases)
directly.
</noscript>

## Verify the installer

Each release ships a `SHA256SUMS.txt` with one line per asset.

=== "Ubuntu / macOS"

    ```bash
    sha256sum -c SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    Get-FileHash -Algorithm SHA256 .\Cuvis_C_SDK_Installer_*.exe
    # Compare against the matching line in SHA256SUMS.txt.
    ```

## After install

The SDK ships a couple of CLI tools and headers under `/opt/cuvis/` (Linux) or
`C:\Program Files\Cuvis\` (Windows). Pick a language wrapper to start writing
code:

- C wrapper: [`cuvis.c`](https://github.com/cubert-hyperspectral/cuvis.c)
- C++ wrapper: [`cuvis.cpp`](https://github.com/cubert-hyperspectral/cuvis.cpp)
- C# wrapper: [`cuvis.csharp`](https://github.com/cubert-hyperspectral/cuvis.csharp)
- Python wrapper: [`cuvis.python`](https://github.com/cubert-hyperspectral/cuvis.python)

Or skim [`examples/`](https://github.com/cubert-hyperspectral/cuvis.sdk/tree/main/examples)
in the umbrella repo for runnable starter code in each language.

## Older releases

The selector lists every published release tag with assets attached. If a
release you need doesn't appear, check the
[full list on GitHub](https://github.com/cubert-hyperspectral/cuvis.sdk/releases?q=&expanded=true)
— some pre-3.4.x releases predate the GitHub Releases hosting and may live
elsewhere.
