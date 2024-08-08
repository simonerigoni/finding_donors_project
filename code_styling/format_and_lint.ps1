# Run autopep8 and pycodestyle on the specified files
# ./format_and_lint.ps1

# Change to the parent directory
cd ..

# Define the files to be processed
$files = Get-ChildItem -Path . -Filter *.py -Recurse | Where-Object { $_.FullName -notmatch "\\.venv\\" }

# Activate the virtual environment
# Note: The activation command varies based on the operating system and shell
# For Windows PowerShell:
& .\.venv\Scripts\Activate.ps1

# For macOS/Linux or Windows using WSL:
# source .venv/bin/activate

# Loop through each file and run autopep8 and pycodestyle
foreach ($file in $files) {
    # Get the full path of the file
    $filePath = $file.FullName

    # Get the base name of the file (e.g., "configuration" from "configuration.py")
    $basename = [System.IO.Path]::GetFileNameWithoutExtension($filePath)

    Write-Host "Processing $filePath..."

    # Automatically format the file to conform to PEP 8
    & autopep8 --in-place $filePath

    # Check the file for PEP 8 compliance and save the report
    & pycodestyle $filePath > ".\code_styling\${basename}_report.txt"

    Write-Host "Report saved to .\code_styling\${basename}_report.txt"
}

# Deactivate the virtual environment after installation (optional)
deactivate