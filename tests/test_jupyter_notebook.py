# Test Jupyter notebook
#
# python test_jupyter_notebook.py


import subprocess


def test_jupyter_notebook():
    # ipython -c "%run finding_donors.ipynb"
    result = subprocess.run(
        ["ipython", "-c", '"%run finding_donors.ipynb"'],
        capture_output=True,  # Capture stdout and stderr
        text=True             # Get output as string
    )

    if result.returncode != 0:
        # print("stderr:", result.stderr)
        print("stdout:", result.stdout)
        test_result = False
    else:
        # print("stdout:", result.stdout)
        test_result = True
    assert test_result
