import os

root_dir_path = 'my_project'
dirs_path = ('settings', 'authapp', 'adminapp', 'authapp')
for dir in dirs_path:
    dir_path = os.path.join(root_dir_path, dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
