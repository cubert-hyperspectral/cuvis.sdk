[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string] $Version,

    [string] $AssetsDir = '_assets',

    [string] $StagingDir = '_assets/.staging',

    [string] $Repo = 'cubert-hyperspectral/cuvis.sdk',

    [string] $LintScript = 'scripts/lint-release-assets.ps1',

    [switch] $Upload
)

# Stage a downloaded Cuvis SDK version (under _assets/Cuvis <ver>/) into a flat
# release-asset layout matching the canonical naming grammar, generate sha256
# sidecars, run the lint script, and optionally upload to the matching GitHub
# release with `gh release upload --clobber`.

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$srcDir = Join-Path $AssetsDir "Cuvis $Version"
$outDir = Join-Path $StagingDir "v$Version"

if (-not (Test-Path -LiteralPath $srcDir -PathType Container)) {
    throw "Source dir not found: $srcDir`nRun:  pwsh scripts/fetch-installers.ps1 -Versions $Version"
}

# --- Helpers ---

function ConvertTo-OsToken {
    param([Parameter(Mandatory)] [string] $ParentDir)
    if ($ParentDir -match '^(?<os>Windows|macOS)\s(?<arch>amd64|arm64)-(?<cuda>nocuda|cuda[\d.]+)$') {
        return [pscustomobject]@{
            Os   = $Matches.os
            Arch = $Matches.arch
            Cuda = $Matches.cuda
        }
    }
    if ($ParentDir -match '^Ubuntu\s(?<osver>[\d.]+)-(?<arch>amd64|arm64)-(?<cuda>nocuda|cuda[\d.]+)(?:-(?<variant>[\w-]+))?$') {
        $os = "Ubuntu$($Matches.osver)"
        if ($Matches.ContainsKey('variant') -and $Matches.variant) {
            $os = "$os-$($Matches.variant)"
        }
        return [pscustomobject]@{
            Os   = $os
            Arch = $Matches.arch
            Cuda = $Matches.cuda
        }
    }
    throw "Unrecognised parent-dir name: '$ParentDir'"
}

$rxBinary = '^(?<pkg>Cuvis_C_SDK_Installer|libcuvis|cuviscommon)_(?<pkgver>[0-9.]+(?:-[0-9]+)?)\.(?<ext>exe|deb|msi|dmg|pkg|tar\.gz)$'

function Get-FlatBinaryName {
    param(
        [Parameter(Mandatory)] [string] $FileName,
        [Parameter(Mandatory)] [object] $OsToken
    )
    if ($FileName -notmatch $rxBinary) {
        throw "Source file '$FileName' doesn't match installer/package grammar"
    }
    $pkg    = $Matches.pkg
    $pkgver = $Matches.pkgver
    $ext    = $Matches.ext
    return "${pkg}_${pkgver}_$($OsToken.Os)_$($OsToken.Arch)_$($OsToken.Cuda).${ext}"
}

# --- Plan rename map ---

$plan = New-Object System.Collections.Generic.List[object]

# Top-level files (PDFs + the source-side SHA256SUMS.txt, which we drop).
foreach ($entry in (Get-ChildItem -LiteralPath $srcDir -File)) {
    if ($entry.Name -ieq 'SHA256SUMS.txt') {
        continue   # regenerated from staged names below
    }
    if ($entry.Name -ieq 'Release Notes.pdf') {
        $plan.Add([pscustomobject]@{
            Source = $entry.FullName
            Target = "RELEASE-NOTES_v${Version}.pdf"
        })
        continue
    }
    if ($entry.Name -match '^Application_Notes_Cuvis_SDK_(?<topic>.+)\.pdf$') {
        $plan.Add([pscustomobject]@{
            Source = $entry.FullName
            Target = "Application-Notes_Cuvis-SDK_$($Matches.topic).pdf"
        })
        continue
    }
    Write-Warning "Unrecognised top-level file '$($entry.Name)' — passing through unchanged"
    $plan.Add([pscustomobject]@{
        Source = $entry.FullName
        Target = $entry.Name
    })
}

# Per-OS-variant subdirectories.
foreach ($subdir in (Get-ChildItem -LiteralPath $srcDir -Directory)) {
    $osTok = ConvertTo-OsToken -ParentDir $subdir.Name
    foreach ($file in (Get-ChildItem -LiteralPath $subdir.FullName -File)) {
        $target = Get-FlatBinaryName -FileName $file.Name -OsToken $osTok
        $plan.Add([pscustomobject]@{
            Source = $file.FullName
            Target = $target
        })
    }
}

# Detect target-name collisions (would clobber on copy).
$collisions = $plan | Group-Object Target | Where-Object Count -gt 1
if ($collisions) {
    foreach ($c in $collisions) {
        Write-Host "Collision on '$($c.Name)':" -ForegroundColor Red
        $c.Group | ForEach-Object { Write-Host "  $($_.Source)" }
    }
    throw "Target-name collisions detected — refusing to stage"
}

# --- Reset & populate staging dir ---

if (Test-Path -LiteralPath $outDir) {
    if ($PSCmdlet.ShouldProcess($outDir, 'Clear staging dir')) {
        Remove-Item -LiteralPath $outDir -Recurse -Force
    }
}
if ($PSCmdlet.ShouldProcess($outDir, 'Create staging dir')) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

Write-Host ""
Write-Host "Staging $($plan.Count) assets to $outDir" -ForegroundColor Cyan
foreach ($p in $plan) {
    $tgt = Join-Path $outDir $p.Target
    if ($PSCmdlet.ShouldProcess($p.Source, "Copy to $tgt")) {
        Copy-Item -LiteralPath $p.Source -Destination $tgt -Force
        Write-Host "  [stage] $($p.Target)" -ForegroundColor DarkGreen
    }
}

# --- aggregate SHA256SUMS.txt ---
#
# We deliberately don't write per-file `.sha256` sidecars: they double the
# release-page asset count for marginal benefit, and SHA256SUMS.txt already
# carries the same data. Tools that want a single-line hash can `grep <name>
# SHA256SUMS.txt` or use the GitHub API's per-asset `digest` field.

Write-Host ""
Write-Host "Hashing..." -ForegroundColor Cyan
$staged = Get-ChildItem -LiteralPath $outDir -File `
    | Where-Object { $_.Name -ne 'SHA256SUMS.txt' } `
    | Sort-Object Name

$sumsLines = New-Object System.Collections.Generic.List[string]
foreach ($s in $staged) {
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $s.FullName).Hash.ToLower()
    $sumsLines.Add("${hash}  $($s.Name)")
}
$sumsPath = Join-Path $outDir 'SHA256SUMS.txt'
if ($PSCmdlet.ShouldProcess($sumsPath, 'Write SHA256SUMS.txt')) {
    Set-Content -LiteralPath $sumsPath -Value (($sumsLines -join "`n") + "`n") -Encoding ascii -NoNewline
    Write-Host "  [sums] $sumsPath ($($sumsLines.Count) entries)"
}

# --- Lint ---

Write-Host ""
Write-Host "Linting staged asset names..." -ForegroundColor Cyan
& $LintScript -Path $outDir
if ($LASTEXITCODE -ne 0) {
    throw "Lint failed — refusing to upload"
}

# --- Upload ---

if ($Upload) {
    $finalSet = (Get-ChildItem -LiteralPath $outDir -File | Sort-Object Name).FullName
    Write-Host ""
    Write-Host "Uploading $($finalSet.Count) asset(s) to v$Version on $Repo..." -ForegroundColor Cyan
    if ($PSCmdlet.ShouldProcess("v$Version", 'gh release upload --clobber')) {
        & gh release upload "v$Version" @finalSet --clobber --repo $Repo
        if ($LASTEXITCODE -ne 0) { throw "gh release upload failed" }
    }
}

Write-Host ""
Write-Host "Done. $($plan.Count) asset(s) staged in $outDir" -ForegroundColor Green
