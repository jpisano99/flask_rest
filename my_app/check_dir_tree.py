import os
from my_app.settings import app_cfg


def check_dir_tree():
    print()
    print('Directory Tree Structure')
    print('\tHOME DIRECTORY:', app_cfg['HOME'])
    print('\tWORKING DIRECTORY:', app_cfg['WORKING_DIR'])
    print('\tUPDATES SUB DIRECTORY:', app_cfg['UPDATES_SUB_DIR'])
    print('\tARCHIVES SUB DIRECTORY:', app_cfg['ARCHIVES__SUB_DIR'])
    print()

    tmp_path = os.path.join(app_cfg['HOME'], app_cfg['WORKING_DIR'])
    if os.path.exists(tmp_path) is False:
        os.mkdir(tmp_path)
        print('\tCREATED:', tmp_path)
    else:
        print('\tDirectory already exists:', tmp_path)

    tmp_path = os.path.join(app_cfg['HOME'], app_cfg['WORKING_DIR'])
    tmp_path = os.path.join(tmp_path, app_cfg['ARCHIVES__SUB_DIR'])
    if os.path.exists(tmp_path) is False:
        os.mkdir(tmp_path)
        print('\tCREATED:', tmp_path)
    else:
        print('\tDirectory already exists:', tmp_path)

    tmp_path = os.path.join(app_cfg['HOME'], app_cfg['WORKING_DIR'])
    tmp_path = os.path.join(tmp_path, app_cfg['UPDATES_SUB_DIR'])
    if os.path.exists(tmp_path) is False:
        os.mkdir(tmp_path)
        print('\tCREATED:', tmp_path)
    else:
        print('\tDirectory already exists:', tmp_path)

    print()
    return
