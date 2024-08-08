# Setup the virtual enviroment. Launch it from within others folder
# ./setup.ps1

# Change to the parent directory
cd ..

# Delete the .venv directory and all its contents if it exists
if (Test-Path -Path .\.venv) {
    Remove-Item -Recurse -Force .\.venv
}

# Create a Python virtual environment in the .venv directory
python -m venv .venv

# Activate the virtual environment
# Note: The activation command varies based on the operating system and shell
# For Windows PowerShell:
& .\.venv\Scripts\Activate.ps1

# For macOS/Linux or Windows using WSL:
# source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Deactivate the virtual environment after installation (optional)
deactivate
