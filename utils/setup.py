# Setup
#
# python -m utils.setup

import os


import utils.configuration as conf


def create_folders(folders=[conf.DATA_FOLDER, conf.IMAGES_FOLDER]):
    """
    Create folders.

    Parameters:
        None

    Returns:
        None
    """
    if isinstance(folders, list):
        pass
    elif isinstance(folders, str):
        folders = [folders]
    else:
        raise ValueError("Error: Input must be a list or a string")

    for current_folder in folders:
        if not os.path.exists(current_folder):
            os.makedirs(current_folder)
            print(f"Folder '{current_folder}' created.")
        else:
            print(f"Folder '{current_folder}' already exists.")


if __name__ == "__main__":
    print("Setup")
    create_folders()
else:
    pass
