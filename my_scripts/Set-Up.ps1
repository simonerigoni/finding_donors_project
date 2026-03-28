# Set up
# .\my_scripts\Set-Up.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

# Stop on any error for robust execution
$ErrorActionPreference = "Stop"

Write-Host "Starting setup process..." -ForegroundColor Green

foreach ($tool in $tools) {
    Write-Host "$(Test-Command $tool.Cmd)..."
    if (Test-Command $tool.Cmd) {
        Write-Host "$($tool.Name) is installed."
    } else {
        Write-Host "$($tool.Name) not found. Installing..."
        if ($tool.InstallMethod -eq 'winget') {
            winget install $tool.InstallId
        } else {
            if ($tool.InstallMethod -eq 'npm') {
                npm install -g $tool.InstallId --unsafe-perm true
            } else {
                Write-Host "Skipping $($tool.Name). It requires $($tool.InstallMethod) but was not found."
            }
        }
        Refresh-Path
    }
}

Write-Host "Running install pre-commit..."
python -m pip install --upgrade pip

Write-Host "Running install pre-commit..."
pip install pre-commit

Write-Host "Install the pre-commit hooks..."
pre-commit install

Write-Host "Running uv sync..."
uv sync

Write-Host "Setup complete! Your Python project environment is ready. Please refresh your shell or restart for PATH updates." -ForegroundColor Green