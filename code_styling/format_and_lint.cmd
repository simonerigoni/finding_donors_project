rem Run autopep8 and pycodestyle on the specified files
rem ./format_and_lint.cmd

@echo off
setlocal

rem Define the files to be processed
set "FILES=..\utils\configuration.py ..\utils\visuals.py ..\tests\test_configuration.py ..\tests\test_jupyter_notebook.py ..\tests\test_visuals.py"

rem Loop through each file and run autopep8 and pycodestyle
for %%f in (%FILES%) do (
    rem Get the base name of the file (e.g., "configuration" from "configuration.py")
    for %%b in (%%~nf) do (
        echo Processing %%f...

        rem Automatically format the file to conform to PEP 8
        autopep8 --in-place %%f

        rem Check the file for PEP 8 compliance and save the report
        pycodestyle %%f > .\%%~nf_report.txt

        echo Report saved to .\%%~nf_report.txt
    )
)

endlocal
