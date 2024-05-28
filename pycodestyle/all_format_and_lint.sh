#!/bin/bash

# Run autopep8 and pycodestyle on the specified files
# chmod +x format_and_lint.sh
# ./all_format_check.sh

# Define the files to be processed
FILES=(
    "../configuration.py"
    "..\visuals.py",
    "..\tests\test_configuration.py",
    "..\tests\test_jupyter_notebook.py",
    "..\tests\test_visuals.py"
)

# Loop through each file and run autopep8 and pycodestyle
for file in "${FILES[@]}"
do
    # Get the base name of the file (e.g., "configuration" from "configuration.py")
    BASENAME=$(basename "$file" .py)

    echo "Processing $file..."

    # Automatically format the file to conform to PEP 8
    autopep8 --in-place "$file"

    # Check the file for PEP 8 compliance and save the report
    pycodestyle "$file" > "./${BASENAME}_report.txt"

    echo "Report saved to ./${BASENAME}_report.txt"
done
