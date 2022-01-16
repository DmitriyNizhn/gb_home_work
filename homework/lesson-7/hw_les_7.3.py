import os
import shutil

root_dir = 'my_project'
search = 'templates'
for root, dirs, files in os.walk(root_dir):
    for dir in dirs:
        if dir == search:
            src = os.path.abspath(os.path.join(root, dir))
            dst = search
            shutil.copytree(src, dst, dirs_exist_ok=True)

src = os.path.abspath(os.path.join(search))
dst = os.path.abspath(os.path.join(root_dir + f'\{search}'))
shutil.copytree(src, dst, dirs_exist_ok=True)
shutil.rmtree(src)
