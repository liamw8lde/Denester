<#
.SYNOPSIS
    Packages or uploads all files from local Windows folder E:\Denester_Fault into the reorganized
    GitHub repository structure (00_Legacy_Baseline/Denester_Fault/).

.DESCRIPTION
    Because Antigravity remote cloud workspaces run in an isolated Linux VM and cannot directly
    mount local Windows drives (E:\), run this script in PowerShell on your Windows PC in one of two modes:
      1. -Mode Zip (Default): Creates E:\Denester_Fault_Upload.zip ready to drag-and-drop into the Antigravity chat.
      2. -Mode GitPush: Clones/pulls https://github.com/liamw8lde/Denester, copies and categorizes all files
         from E:\Denester_Fault into 00_Legacy_Baseline/Denester_Fault/, and pushes a commit/branch to GitHub.

.EXAMPLE
    .\upload_denester_fault.ps1 -SourcePath "E:\Denester_Fault" -Mode Zip
    .\upload_denester_fault.ps1 -SourcePath "E:\Denester_Fault" -Mode GitPush -Branch "feat/gamp5-phase1-and-repo-reorg"
#>

param(
    [string]$SourcePath = "E:\Denester_Fault",
    [ValidateSet("Zip", "GitPush")]
    [string]$Mode = "Zip",
    [string]$RepoUrl = "https://github.com/liamw8lde/Denester.git",
    [string]$Branch = "feat/gamp5-phase1-and-repo-reorg"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $SourcePath)) {
    Write-Error "Source folder '$SourcePath' was not found on this machine. Check that drive E: is connected."
    exit 1
}

if ($Mode -eq "Zip") {
    $ZipOut = Join-Path (Split-Path -Parent $SourcePath) "Denester_Fault_Upload.zip"
    if (Test-Path -LiteralPath $ZipOut) {
        Remove-Item -LiteralPath $ZipOut -Force
    }
    Write-Host "Compressing '$SourcePath' -> '$ZipOut' ..." -ForegroundColor Cyan
    Compress-Archive -Path (Join-Path $SourcePath "*") -DestinationPath $ZipOut -CompressionLevel Optimal
    $SizeMB = [math]::Round((Get-Item $ZipOut).Length / 1MB, 2)
    Write-Host "Done! Created '$ZipOut' ($SizeMB MB)." -ForegroundColor Green
    Write-Host "Next step: Drag and drop '$ZipOut' directly into the Antigravity chat window so the agent can unpack and organize every file." -ForegroundColor Yellow
    exit 0
}

# Mode = GitPush: Clone repo to temp workspace, categorize files, commit & push
$TempClone = Join-Path $env:TEMP ("Denester_Sync_" + [guid]::NewGuid().ToString("N").Substring(0, 8))
Write-Host "Cloning $RepoUrl (branch: $Branch) into $TempClone ..." -ForegroundColor Cyan
git clone --branch $Branch $RepoUrl $TempClone

$TargetRoot = Join-Path $TempClone "00_Legacy_Baseline\Denester_Fault"
$SubDirs = @(
    "Schematics_and_Manuals",
    "PLC_and_HMI_Exports",
    "Fault_Logs_and_Notes",
    "Photos_and_Videos",
    "Other_Legacy_Files"
)
foreach ($d in $SubDirs) {
    New-Item -ItemType Directory -Force -Path (Join-Path $TargetRoot $d) | Out-Null
}

$Files = Get-ChildItem -LiteralPath $SourcePath -Recurse -File | Where-Object {
    $_.FullName -notmatch "\\\.git\\"
}

foreach ($f in $Files) {
    $ext = $f.Extension.ToLowerInvariant()
    $relParent = $f.DirectoryName.Substring($SourcePath.TrimEnd('\').Length).TrimStart('\')
    switch -Regex ($ext) {
        "^\.(pdf|dwg|dxf|eplan|zw1)$"               { $cat = "Schematics_and_Manuals" }
        "^\.(s7p|zap\d*|ap\d*|awl|scl|sdf|pdb|psb|zip)$" { $cat = "PLC_and_HMI_Exports" }
        "^\.(txt|md|doc|docx|xls|xlsx|csv|log)$"    { $cat = "Fault_Logs_and_Notes" }
        "^\.(png|jpg|jpeg|bmp|gif|mp4|mov)$"        { $cat = "Photos_and_Videos" }
        default                                     { $cat = "Other_Legacy_Files" }
    }
    $destDir = if ($relParent) { Join-Path (Join-Path $TargetRoot $cat) $relParent } else { Join-Path $TargetRoot $cat }
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    Copy-Item -LiteralPath $f.FullName -Destination (Join-Path $destDir $f.Name) -Force
}

Push-Location $TempClone
try {
    git add "00_Legacy_Baseline/Denester_Fault"
    git status --short
    git commit -m "chore(legacy): import and categorize E:\Denester_Fault archive into 00_Legacy_Baseline"
    git push origin $Branch
    Write-Host "Successfully uploaded and organized '$SourcePath' to GitHub ($Branch)!" -ForegroundColor Green
} finally {
    Pop-Location
}
