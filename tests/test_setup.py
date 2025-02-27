# Test setup
#
# python test_setup.py

import os
import shutil


import utils.setup as setu


def test_create_folders():
    test_folder = 'test_folder'
    if not os.path.exists(test_folder):
        pass
    else:
        shutil.rmtree(test_folder)

    setu.create_folders(test_folder)
    test_result = os.path.exists(test_folder)
    shutil.rmtree(test_folder)
    assert test_result
