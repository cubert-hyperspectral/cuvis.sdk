/* Cuvis SDK installer selector.
 *
 * Vanilla JS, no framework. Subscribes to Material's `document$` observable
 * (Material `navigation.instant` swaps `document.body` on internal nav clicks
 * — without this rebind the form dies after the first nav).
 *
 * Caches the GitHub Releases response in localStorage for 30 min — required,
 * not optional, because unauthenticated GitHub API is 60 req/hour/IP.
 */
(function () {
  "use strict";

  const REPO = "cubert-hyperspectral/cuvis.sdk";
  const API_URL = `https://api.github.com/repos/${REPO}/releases?per_page=100`;
  const CACHE_KEY = "cuvisSdk.releases.v1";
  const CACHE_TTL_MS = 30 * 60 * 1000;

  // Pattern A — installers/packages (drives the dropdowns).
  const RX_INSTALLER =
    /^(?<pkg>Cuvis_C_SDK_Installer|libcuvis|cuviscommon)_(?<pkgver>[0-9.]+(?:-[0-9]+)?)_(?<os>Windows|macOS|Ubuntu[0-9.]+(?:-jetson(?:-experimental)?)?)_(?<arch>amd64|arm64)_(?<cuda>nocuda|cuda[0-9.]+)\.(?<ext>exe|deb|msi|dmg|pkg|tar\.gz)$/;

  // Pattern B — release metadata.
  const RX_METADATA =
    /^(SHA256SUMS\.txt|.+\.sha256|RELEASE-NOTES(?:_v[0-9.]+)?\.pdf|Application-Notes_Cuvis-SDK(?:_[A-Za-z0-9-]+)?\.pdf|.+\.pdf|README\.md|RELEASE-NOTES\.md)$/;

  const PKG_ROLE = {
    Cuvis_C_SDK_Installer: "installer",
    libcuvis: "libcuvis",
    cuviscommon: "cuviscommon",
  };

  const OS_LABEL = {
    Windows: "Windows",
    macOS: "macOS",
    "Ubuntu20.04": "Ubuntu 20.04",
    "Ubuntu22.04": "Ubuntu 22.04",
    "Ubuntu24.04": "Ubuntu 24.04",
    "Ubuntu20.04-jetson": "Ubuntu 20.04 (Jetson)",
    "Ubuntu22.04-jetson": "Ubuntu 22.04 (Jetson)",
    "Ubuntu24.04-jetson": "Ubuntu 24.04 (Jetson)",
    "Ubuntu20.04-jetson-experimental": "Ubuntu 20.04 (Jetson, experimental)",
    "Ubuntu22.04-jetson-experimental": "Ubuntu 22.04 (Jetson, experimental)",
    "Ubuntu24.04-jetson-experimental": "Ubuntu 24.04 (Jetson, experimental)",
  };

  function osLabel(os) {
    return OS_LABEL[os] || os;
  }

  function cudaLabel(cuda) {
    return cuda === "nocuda" ? "No CUDA" : cuda.replace(/^cuda/, "CUDA ");
  }

  function readCache() {
    try {
      const raw = localStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      const obj = JSON.parse(raw);
      if (Date.now() - obj.fetchedAt > CACHE_TTL_MS) return null;
      return obj.releases;
    } catch (_) {
      return null;
    }
  }

  function writeCache(releases) {
    try {
      localStorage.setItem(
        CACHE_KEY,
        JSON.stringify({ fetchedAt: Date.now(), releases })
      );
    } catch (_) {
      // localStorage full or disabled — silently skip.
    }
  }

  async function fetchReleases() {
    const cached = readCache();
    if (cached) return cached;
    const resp = await fetch(API_URL, {
      headers: { Accept: "application/vnd.github+json" },
    });
    if (!resp.ok) {
      throw new Error(`GitHub API ${resp.status}: ${resp.statusText}`);
    }
    const releases = await resp.json();
    writeCache(releases);
    return releases;
  }

  function parsePatternA(asset) {
    const m = RX_INSTALLER.exec(asset.name);
    if (!m) return null;
    return {
      name: asset.name,
      url: asset.browser_download_url,
      ...m.groups,
    };
  }

  function parsePatternB(asset) {
    if (!RX_METADATA.test(asset.name)) return null;
    if (RX_INSTALLER.test(asset.name)) return null;
    return { name: asset.name, url: asset.browser_download_url };
  }

  function indexRelease(release) {
    const patternA = [];
    const patternB = [];
    for (const a of release.assets || []) {
      const pa = parsePatternA(a);
      if (pa) {
        patternA.push(pa);
        continue;
      }
      const pb = parsePatternB(a);
      if (pb) patternB.push(pb);
    }
    return { release, patternA, patternB };
  }

  function el(tag, attrs, ...children) {
    const node = document.createElement(tag);
    if (attrs) {
      for (const [k, v] of Object.entries(attrs)) {
        if (k === "className") node.className = v;
        else if (k === "textContent") node.textContent = v;
        else node.setAttribute(k, v);
      }
    }
    for (const c of children) {
      if (c == null) continue;
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    }
    return node;
  }

  function uniqueSorted(values, cmp) {
    const arr = [...new Set(values)];
    arr.sort(cmp || ((a, b) => a.localeCompare(b)));
    return arr;
  }

  function buildSelect(id, labelText, options, selected, onChange) {
    const wrap = el("label", { className: "sdk-installer__field", for: id });
    wrap.appendChild(
      el("span", { className: "sdk-installer__label", textContent: labelText })
    );
    const sel = el("select", { id, className: "sdk-installer__select" });
    for (const o of options) {
      const opt = el("option", { value: o.value, textContent: o.label });
      if (o.value === selected) opt.selected = true;
      sel.appendChild(opt);
    }
    sel.addEventListener("change", onChange);
    wrap.appendChild(sel);
    return { wrap, select: sel };
  }

  function renderInstallCommand(osBucket, byRole) {
    if (osBucket === "Ubuntu") {
      const common = byRole.cuviscommon;
      const lib = byRole.libcuvis;
      if (!common || !lib) return null;
      return [
        `curl -O ${common.url}`,
        `curl -O ${lib.url}`,
        "sudo dpkg -i cuviscommon_*.deb libcuvis_*.deb",
      ].join("\n");
    }
    if (osBucket === "Windows") {
      const installer = byRole.installer;
      if (!installer) return null;
      return [
        `Invoke-WebRequest -Uri ${installer.url} -OutFile ${installer.name}`,
        `Start-Process -Wait -FilePath .\\${installer.name}`,
      ].join("\n");
    }
    if (osBucket === "macOS") {
      const installer = byRole.installer;
      if (!installer) return null;
      return [
        `curl -O ${installer.url}`,
        `# Open ${installer.name} and follow the installer prompts`,
      ].join("\n");
    }
    return null;
  }

  function renderError(form, msg) {
    form.innerHTML = "";
    const note = el("div", { className: "sdk-installer__error" });
    note.appendChild(el("p", { textContent: msg }));
    note.appendChild(
      el(
        "p",
        {},
        "Browse all installers on ",
        el("a", {
          href: `https://github.com/${REPO}/releases`,
          textContent: "GitHub Releases",
        }),
        "."
      )
    );
    form.appendChild(note);
  }

  function metadataLabel(name) {
    if (name.startsWith("RELEASE-NOTES")) return "Release notes (PDF)";
    if (name.startsWith("Application-Notes_Cuvis-SDK")) {
      const topic = name
        .replace(/^Application-Notes_Cuvis-SDK_?/, "")
        .replace(/\.pdf$/, "");
      return topic ? `Application notes — ${topic} (PDF)` : "Application notes (PDF)";
    }
    if (name === "SHA256SUMS.txt") return "SHA256SUMS.txt (checksums)";
    return null;
  }

  async function run() {
    const form = document.getElementById("cuvis-sdk-installer");
    if (!form) return;

    let releases;
    try {
      releases = await fetchReleases();
    } catch (err) {
      renderError(
        form,
        `Couldn't reach GitHub Releases (${err.message}). Try again in a few minutes.`
      );
      return;
    }
    if (!Array.isArray(releases) || !releases.length) {
      renderError(form, "No releases found.");
      return;
    }

    let includePrerelease = form.dataset.prerelease === "1";
    let includeJetsonExp = form.dataset.jetsonExp === "1";

    function visibleReleases() {
      return includePrerelease
        ? releases
        : releases.filter((r) => !r.prerelease);
    }

    function osIsExperimental(os) {
      return /-jetson-experimental$/.test(os);
    }

    function render() {
      form.innerHTML = "";

      const visible = visibleReleases().filter((r) =>
        (r.assets || []).some((a) => RX_INSTALLER.test(a.name))
      );
      if (!visible.length) {
        renderError(
          form,
          "No releases with installer assets are available. Try toggling pre-release builds."
        );
        // Still render the prerelease toggle below.
      }

      const indexed = visible.map(indexRelease);

      let versionTag =
        form.dataset.version || (indexed[0] && indexed[0].release.tag_name);
      let current =
        indexed.find((i) => i.release.tag_name === versionTag) || indexed[0];
      if (current) versionTag = current.release.tag_name;

      const osesAvailable = current
        ? uniqueSorted(
            current.patternA
              .filter((a) => includeJetsonExp || !osIsExperimental(a.os))
              .map((a) => a.os)
          )
        : [];
      let os =
        form.dataset.os && osesAvailable.includes(form.dataset.os)
          ? form.dataset.os
          : osesAvailable[0];

      const archesAvailable = current
        ? uniqueSorted(
            current.patternA
              .filter((a) => a.os === os)
              .map((a) => a.arch)
          )
        : [];
      let arch =
        form.dataset.arch && archesAvailable.includes(form.dataset.arch)
          ? form.dataset.arch
          : archesAvailable[0];

      const cudasAvailable = current
        ? uniqueSorted(
            current.patternA
              .filter((a) => a.os === os && a.arch === arch)
              .map((a) => a.cuda)
          )
        : [];
      let cuda =
        form.dataset.cuda && cudasAvailable.includes(form.dataset.cuda)
          ? form.dataset.cuda
          : cudasAvailable[0];

      function persist() {
        form.dataset.version = versionTag || "";
        form.dataset.os = os || "";
        form.dataset.arch = arch || "";
        form.dataset.cuda = cuda || "";
        form.dataset.prerelease = includePrerelease ? "1" : "0";
        form.dataset.jetsonExp = includeJetsonExp ? "1" : "0";
      }

      function rerender() {
        persist();
        render();
      }

      const grid = el("div", { className: "sdk-installer__grid" });

      if (current) {
        grid.appendChild(
          buildSelect(
            "sdk-version",
            "Version",
            indexed.map((i) => ({
              value: i.release.tag_name,
              label: i.release.tag_name,
            })),
            versionTag,
            (e) => {
              versionTag = e.target.value;
              os = arch = cuda = undefined;
              form.dataset.os = form.dataset.arch = form.dataset.cuda = "";
              rerender();
            }
          ).wrap
        );
        grid.appendChild(
          buildSelect(
            "sdk-os",
            "OS",
            osesAvailable.map((o) => ({ value: o, label: osLabel(o) })),
            os,
            (e) => {
              os = e.target.value;
              arch = cuda = undefined;
              form.dataset.arch = form.dataset.cuda = "";
              rerender();
            }
          ).wrap
        );
        grid.appendChild(
          buildSelect(
            "sdk-arch",
            "Architecture",
            archesAvailable.map((a) => ({ value: a, label: a })),
            arch,
            (e) => {
              arch = e.target.value;
              cuda = undefined;
              form.dataset.cuda = "";
              rerender();
            }
          ).wrap
        );
        grid.appendChild(
          buildSelect(
            "sdk-cuda",
            "CUDA",
            cudasAvailable.map((c) => ({ value: c, label: cudaLabel(c) })),
            cuda,
            (e) => {
              cuda = e.target.value;
              rerender();
            }
          ).wrap
        );
      }

      form.appendChild(grid);

      // Toggles. Each one drops the cached selection because the visible
      // set changes; the next render() picks the first valid option.
      const toggles = el("div", { className: "sdk-installer__toggles" });

      function makeToggle(labelText, checked, onChange) {
        const wrap = el("label", { className: "sdk-installer__toggle" });
        const box = el("input", { type: "checkbox" });
        box.checked = checked;
        box.addEventListener("change", (e) => onChange(e.target.checked));
        wrap.appendChild(box);
        wrap.appendChild(document.createTextNode(" " + labelText));
        return wrap;
      }

      function clearSelection() {
        versionTag = os = arch = cuda = undefined;
        form.dataset.version = form.dataset.os = form.dataset.arch = form.dataset.cuda = "";
      }

      toggles.appendChild(
        makeToggle("Show pre-release builds", includePrerelease, (checked) => {
          includePrerelease = checked;
          clearSelection();
          rerender();
        })
      );
      toggles.appendChild(
        makeToggle(
          "Show Jetson (experimental) builds",
          includeJetsonExp,
          (checked) => {
            includeJetsonExp = checked;
            clearSelection();
            rerender();
          }
        )
      );
      form.appendChild(toggles);

      if (!current) return;

      const matching = current.patternA.filter(
        (a) => a.os === os && a.arch === arch && a.cuda === cuda
      );
      const output = el("div", { className: "sdk-installer__output" });

      if (!matching.length) {
        output.appendChild(
          el("p", {
            className: "sdk-installer__warning",
            textContent:
              "No installer for this combination on " +
              versionTag +
              ". Try a different OS, arch, or CUDA — or toggle pre-release builds.",
          })
        );
      } else {
        const byRole = {};
        for (const a of matching) byRole[PKG_ROLE[a.pkg]] = a;
        const osBucket = os.startsWith("Ubuntu") ? "Ubuntu" : os;
        const cmd = renderInstallCommand(osBucket, byRole);
        if (cmd) {
          output.appendChild(
            el("h3", {
              className: "sdk-installer__heading",
              textContent: "Install command",
            })
          );
          const pre = el("pre", { className: "sdk-installer__cmd" });
          pre.appendChild(el("code", { textContent: cmd }));
          output.appendChild(pre);
        }
        const dl = el("ul", { className: "sdk-installer__downloads" });
        for (const a of matching) {
          dl.appendChild(
            el(
              "li",
              {},
              el("a", { href: a.url, textContent: a.name })
            )
          );
        }
        const details = el(
          "details",
          { className: "sdk-installer__details" },
          el("summary", { textContent: "Direct download links" }),
          dl
        );
        output.appendChild(details);
      }
      form.appendChild(output);

      // Pattern B — release artifacts.
      const meta = current.patternB
        .map((m) => ({ ...m, label: metadataLabel(m.name) }))
        .filter((m) => m.label);
      if (meta.length) {
        const block = el("div", { className: "sdk-installer__metadata" });
        block.appendChild(
          el("h3", {
            className: "sdk-installer__heading",
            textContent: "Release artifacts",
          })
        );
        const ul = el("ul");
        for (const m of meta) {
          ul.appendChild(
            el("li", {}, el("a", { href: m.url, textContent: m.label }))
          );
        }
        block.appendChild(ul);
        form.appendChild(block);
      }

      form.appendChild(
        el(
          "p",
          { className: "sdk-installer__fallback" },
          "Looking for an older release or a combination not in the dropdowns? See ",
          el("a", {
            href: `https://github.com/${REPO}/releases`,
            textContent: "all releases",
          }),
          "."
        )
      );
    }

    render();
  }

  if (
    typeof document$ !== "undefined" &&
    document$ &&
    typeof document$.subscribe === "function"
  ) {
    document$.subscribe(run);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
