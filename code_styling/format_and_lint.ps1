# Run autopep8 and pycodestyle on the specified files
# ./format_and_lint.ps1

# Define the files to be processed
$files = @(
    "..\configuration.py",
    "..\visuals.py",
    "..\tests\test_configuration.py",
    "..\tests\test_jupyter_notebook.py",
    "..\tests\test_visuals.py"
)

# Loop through each file and run autopep8 and pycodestyle
foreach ($file in $files) {
    # Get the base name of the file (e.g., "configuration" from "configuration.py")
    $basename = [System.IO.Path]::GetFileNameWithoutExtension($file)

    Write-Host "Processing $file..."

    # Automatically format the file to conform to PEP 8
    & autopep8 --in-place $file

    # Check the file for PEP 8 compliance and save the report
    & pycodestyle $file > ".\${basename}_report.txt"

    Write-Host "Report saved to .\${basename}_report.txt"
}
