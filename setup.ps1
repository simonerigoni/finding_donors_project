# Setup the local enviroment
# ./setup.ps1

# Configurable variables
$requirementsFile = "requirements.txt"
$venvDir = ".venv"

# Function to check if a command exists
function Test-CommandExists {
    param ($command)
    try {
        Get-Command $command -ErrorAction Stop | Out-Null
        return $true
    }
    catch {
        return $false
    }
}

# Check if Python is installed
if (-not (Test-CommandExists "python")) {
    Write-Host "Python is not installed or not in PATH. Please make Python available." -ForegroundColor Red
    exit 1
}

# Get Python version
$pythonVersion = python --version
Write-Host "Found $pythonVersion" -ForegroundColor Green

# Check for requirements.txt
if (-not (Test-Path $requirementsFile)) {
    Write-Host "No $requirementsFile found" -ForegroundColor Red
    exit 1
}

# Check if virtual environment exists
if (Test-Path $venvDir) {
    Write-Host "Found virtual environment" -ForegroundColor Yellow
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv $venvDir
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& ".\$venvDir\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing project dependencies..." -ForegroundColor Cyan
pip install -r $requirementsFile
Write-Host "Dependencies installed successfully!" -ForegroundColor Green

# Deactivate virtual environment if it was activated
Write-Host "Deactivating virtual environment..." -ForegroundColor Cyan
deactivate

Write-Host "`nSetup complete! Your Python project environment is ready." -ForegroundColor Green
Write-Host "Note: To activate the virtual environment in future sessions, run: .\$venvDir\Scripts\Activate.ps1"