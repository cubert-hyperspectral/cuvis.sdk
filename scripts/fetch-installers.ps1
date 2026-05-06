[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string[]] $Versions,

    [string] $OutDir = '_assets',

    [string] $ShareToken = 'qpxkyWkycrmBK9m',

    [string] $WebdavRoot = 'https://cloud.cubert-gmbh.de/public.php/webdav/'
)

# Mirror Cuvis C SDK installer share (Nextcloud public link) into a local folder
# so that scripts/stage-release-assets.ps1 can rename + upload them to GitHub Releases.
#
# Idempotent / resumable: files whose on-disk size matches WebDAV getcontentlength
# are skipped. Writes a SHA256SUMS.txt per version directory.

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# Nextcloud's `-Credential -Authentication Basic` route returns 401 for share-token
# auth (empty password). Setting the Authorization header by hand works.
$auth = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("${ShareToken}:"))
$baseHeaders = @{ Authorization = $auth }

function Invoke-WebDavPropfind {
    param(
        [Parameter(Mandatory)] [string] $Url,
        [string] $Depth = 'infinity'
    )
    $h = @{ Authorization = $baseHeaders.Authorization; Depth = $Depth }
    # `-Method PROPFIND` is rejected; `-CustomMethod` accepts non-standard verbs.
    $resp = Invoke-WebRequest -Uri $Url -CustomMethod 'PROPFIND' -Headers $h -ErrorAction Stop
    [xml] $resp.Content
}

function Get-DavEntries {
    param(
        [Parameter(Mandatory)] [xml]    $Xml,
        [Parameter(Mandatory)] [string] $BaseUrl
    )
    $nm = New-Object System.Xml.XmlNamespaceManager($Xml.NameTable)
    $nm.AddNamespace('d', 'DAV:')
    $baseUri = [uri] $BaseUrl
    foreach ($node in $Xml.SelectNodes('//d:response', $nm)) {
        $hrefNode = $node.SelectSingleNode('d:href', $nm)
        if (-not $hrefNode) { continue }
        $href = $hrefNode.InnerText

        $isCollection = [bool] $node.SelectSingleNode(
            ".//d:propstat[contains(d:status,'200')]/d:prop/d:resourcetype/d:collection", $nm)

        $size = $null
        $clNode = $node.SelectSingleNode(
            ".//d:propstat[contains(d:status,'200')]/d:prop/d:getcontentlength", $nm)
        if ($clNode) { $size = [int64] $clNode.InnerText }

        [pscustomobject]@{
            Href         = $href
            IsCollection = $isCollection
            Size         = $size
            Url          = ([uri]::new($baseUri, $href)).AbsoluteUri
        }
    }
}

function ConvertTo-LocalPath {
    param(
        [Parameter(Mandatory)] [string] $Href,
        [Parameter(Mandatory)] [string] $OutDir
    )
    # Strip the WebDAV root prefix and percent-decode each path segment so that
    # spaces and special chars become literal filesystem characters.
    $relative = $Href -replace '^/public\.php/webdav/', ''
    $relative = $relative.TrimEnd('/')
    if (-not $relative) { return $null }
    $segments = ($relative -split '/') | ForEach-Object { [uri]::UnescapeDataString($_) }
    return (Join-Path -Path $OutDir -ChildPath ($segments -join [IO.Path]::DirectorySeparatorChar))
}

function Save-DavFile {
    param(
        [Parameter(Mandatory)] [string] $Url,
        [Parameter(Mandatory)] [string] $LocalPath,
        [int64] $ExpectedSize = 0
    )
    $dir = Split-Path -Parent $LocalPath
    if ($dir -and -not (Test-Path -LiteralPath $dir)) {
        if ($PSCmdlet.ShouldProcess($dir, 'Create directory')) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    if (Test-Path -LiteralPath $LocalPath -PathType Leaf) {
        $existingSize = (Get-Item -LiteralPath $LocalPath).Length
        if ($ExpectedSize -gt 0 -and $existingSize -eq $ExpectedSize) {
            Write-Host "  [skip] $LocalPath ($existingSize bytes match)" -ForegroundColor DarkGray
            return
        }
        Write-Host "  [redownload] $LocalPath (have $existingSize, expect $ExpectedSize)" -ForegroundColor Yellow
    }
    if ($PSCmdlet.ShouldProcess($Url, "Download to $LocalPath")) {
        Write-Host "  [get ] $LocalPath" -ForegroundColor Green
        Invoke-WebRequest -Uri $Url -Headers $baseHeaders -OutFile $LocalPath -ErrorAction Stop
    }
}

function Write-Sha256Sums {
    param([Parameter(Mandatory)] [string] $VersionDir)
    if (-not (Test-Path -LiteralPath $VersionDir -PathType Container)) { return }
    $files = Get-ChildItem -LiteralPath $VersionDir -Recurse -File `
        | Where-Object { $_.Name -ne 'SHA256SUMS.txt' } `
        | Sort-Object FullName
    $lines = foreach ($f in $files) {
        $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $f.FullName).Hash.ToLower()
        $rel  = $f.FullName.Substring($VersionDir.Length).TrimStart('\','/').Replace('\','/')
        "${hash}  ${rel}"
    }
    $sumsPath = Join-Path $VersionDir 'SHA256SUMS.txt'
    if ($PSCmdlet.ShouldProcess($sumsPath, 'Write SHA256SUMS.txt')) {
        ($lines -join "`n") + "`n" | Set-Content -LiteralPath $sumsPath -Encoding ascii -NoNewline
        Write-Host "  [sums] $sumsPath ($($files.Count) files)" -ForegroundColor Cyan
    }
}

# --- main ----------------------------------------------------------------

if (-not (Test-Path -LiteralPath $OutDir)) {
    if ($PSCmdlet.ShouldProcess($OutDir, 'Create out dir')) {
        New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
    }
}

foreach ($ver in $Versions) {
    $verFolder = "Cuvis $ver"
    $verUrl    = "$WebdavRoot$([uri]::EscapeDataString($verFolder))/"
    Write-Host ""
    Write-Host "=== Cuvis $ver ===" -ForegroundColor Cyan
    Write-Host "  PROPFIND $verUrl"

    $xml = $null
    try {
        $xml = Invoke-WebDavPropfind -Url $verUrl -Depth 'infinity'
    } catch {
        Write-Warning "  Depth: infinity rejected ($($_.Exception.Message)); falling back to recursive Depth: 1"
    }

    $entries = New-Object System.Collections.Generic.List[object]
    if ($xml) {
        Get-DavEntries -Xml $xml -BaseUrl $WebdavRoot `
            | Where-Object { -not $_.IsCollection -and $_.Size -gt 0 } `
            | ForEach-Object { $entries.Add($_) }
    } else {
        $queue = [System.Collections.Generic.Queue[string]]::new()
        $queue.Enqueue($verUrl)
        $seen = [System.Collections.Generic.HashSet[string]]::new()
        while ($queue.Count -gt 0) {
            $u = $queue.Dequeue()
            if (-not $seen.Add($u.TrimEnd('/'))) { continue }
            $x = Invoke-WebDavPropfind -Url $u -Depth '1'
            foreach ($it in (Get-DavEntries -Xml $x -BaseUrl $WebdavRoot)) {
                if ($it.Url.TrimEnd('/') -eq $u.TrimEnd('/')) { continue }
                if ($it.IsCollection) { $queue.Enqueue($it.Url) }
                elseif ($it.Size -gt 0) { $entries.Add($it) }
            }
        }
    }

    Write-Host ("  found {0} files" -f $entries.Count)

    foreach ($e in $entries) {
        $local = ConvertTo-LocalPath -Href $e.Href -OutDir $OutDir
        if (-not $local) { continue }
        Save-DavFile -Url $e.Url -LocalPath $local -ExpectedSize $e.Size
    }

    Write-Sha256Sums -VersionDir (Join-Path $OutDir $verFolder)
}

Write-Host ""
Write-Host "Done." -ForegroundColor Green
