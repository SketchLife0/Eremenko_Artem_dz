import os
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(base_dir, '')
for path, folders, files in os.walk(project_dir):
    for folder in folders:
        if folder == 'templates':
            direct = os.path.join(path, folder)
            shutil.copytree(direct, 'my_project/templates', dirs_exist_ok=True)
