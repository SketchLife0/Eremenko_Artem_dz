import os

def create_directory(name_project, *args):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    new_path = os.path.join(base_dir, name_project)
    if not os.path.exists(new_path):
        os.mkdir(name_project)
    os.chdir(new_path)
    for elem in args:
        interior_new_path = os.path.join(new_path, elem)
        if not os.path.exists(interior_new_path):
            os.mkdir(elem)


create_directory('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')