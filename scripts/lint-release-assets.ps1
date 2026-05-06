[CmdletBinding(DefaultParameterSetName = 'Names')]
param(
    [Parameter(ParameterSetName = 'Names', Mandatory)]
    [string[]] $Names,

    [Parameter(ParameterSetName = 'Tag', Mandatory)]
    [string] $Tag,

    [Parameter(ParameterSetName = 'Path', Mandatory)]
    [string] $Path,

    [string] $Repo = 'cubert-hyperspectral/cuvis.sdk'
)

# Validates GitHub-Release asset names against the canonical Cuvis SDK grammar.
# Every uploaded asset must match Pattern A (installers/packages — drives the
# selector dropdowns) or Pattern B (release metadata — surfaced as named links).
# Anything else fails.

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# Pattern A — installers/packages
$RegexInstaller = '^(?<pkg>Cuvis_C_SDK_Installer|libcuvis|cuviscommon)_(?<pkgver>[0-9.]+(?:-[0-9]+)?)_(?<os>Windows|macOS|Ubuntu[0-9.]+(?:-jetson(?:-experimental)?)?)_(?<arch>amd64|arm64)_(?<cuda>nocuda|cuda[0-9.]+)\.(?<ext>exe|deb|msi|dmg|pkg|tar\.gz)$'

# Pattern B — release metadata
$RegexMetadata = '^(SHA256SUMS\.txt|.+\.sha256|RELEASE-NOTES(?:_v[0-9.]+)?\.pdf|Application-Notes_Cuvis-SDK(?:_[A-Za-z0-9-]+)?\.pdf|.+\.pdf|README\.md|RELEASE-NOTES\.md)$'

# Resolve the asset name set from the chosen parameter set.
$resolved = switch ($PSCmdlet.ParameterSetName) {
    'Names' { $Names }
    'Tag' {
        $json = & gh release view $Tag --repo $Repo --json assets 2>$null
        if ($LASTEXITCODE -ne 0 -or -not $json) {
            throw "gh release view '$Tag' --repo $Repo failed"
        }
        @(($json | ConvertFrom-Json).assets.name)
    }
    'Path' {
        if (-not (Test-Path -LiteralPath $Path)) {
            throw "Path not found: $Path"
        }
        @((Get-ChildItem -LiteralPath $Path -File -Recurse).Name)
    }
}

if (-not $resolved -or $resolved.Count -eq 0) {
    Write-Warning "No asset names to lint."
    exit 0
}

$failed = @()
foreach ($n in $resolved) {
    if (-not $n) { continue }
    if ($n -match $RegexInstaller) {
        Write-Host "  [ok-A] $n" -ForegroundColor DarkGreen
    } elseif ($n -match $RegexMetadata) {
        Write-Host "  [ok-B] $n" -ForegroundColor DarkCyan
    } else {
        $failed += $n
        Write-Host "  [FAIL] $n" -ForegroundColor Red
    }
}

Write-Host ""
if ($failed.Count -gt 0) {
    Write-Host ("{0} asset name(s) failed pattern check:" -f $failed.Count) -ForegroundColor Red
    $failed | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    Write-Host ""
    Write-Host "Pattern A (installers/packages):" -ForegroundColor Yellow
    Write-Host "  $RegexInstaller"
    Write-Host "Pattern B (release metadata):" -ForegroundColor Yellow
    Write-Host "  $RegexMetadata"
    exit 1
}

Write-Host ("All {0} asset name(s) valid." -f $resolved.Count) -ForegroundColor Green
exit 0
