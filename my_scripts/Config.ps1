# Config
# .\my_scripts\Config.ps1

$venvFolder = ".venv"

function Refresh-Path {
    $env:PATH = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

function Test-Command {
    param([string]$Command)
    $old = $ErrorActionPreference
    $ErrorActionPreference = 'SilentlyContinue'
    try {
        $output = & $Command --version 2>&1
        return $output -match '\d+\.\d+'
    } catch {
            return $false
    } finally {
            $ErrorActionPreference = $old
    }
}

$tools = @(
    @{Name='Python'; Cmd='python'; InstallMethod='winget'; InstallId='Python.Python.3.11'},
    @{Name='uv'; Cmd='uv'; InstallMethod='winget'; InstallId='astral-sh.uv'}
)