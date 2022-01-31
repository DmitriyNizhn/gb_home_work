import os

root_dir_path = 'my_project'
dirs_path = ('settings', 'mainapp', 'authapp')
templats = 'templates'
for dir in dirs_path:
    dir_path = os.path.join(root_dir_path, dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
with open(f'{root_dir_path}/{dirs_path[0]}/__init__.py', 'w', encoding='utf-8') as f1, \
        open(f'{root_dir_path}/{dirs_path[0]}/dev.py', 'w', encoding='utf-8') as f2, \
        open(f'{root_dir_path}/{dirs_path[0]}/prod.py', 'w', encoding='utf-8') as f3:
    f1.write('new project')
    f2.write('new project')
    f3.write('new project')

for dir in ('mainapp', 'authapp'):
    with open(f'{root_dir_path}/{dir}/__init__.py', 'w', encoding='utf-8') as f1, \
            open(f'{root_dir_path}/{dir}/models.py', 'w', encoding='utf-8') as f2, \
            open(f'{root_dir_path}/{dir}/views.py', 'w', encoding='utf-8') as f3:
        f1.write('new project')
        f2.write('new project')
        f3.write('new project')
    os.makedirs(f'{root_dir_path}/{dir}/{templats}/{dir}', exist_ok=True)
    with open(f'{root_dir_path}/{dir}/{templats}/{dir}/base.html', 'w', encoding='utf-8') as f4, \
            open(f'{root_dir_path}/{dir}/{templats}/{dir}/index.html', 'w', encoding='utf-8') as f5:
        f4.write('new project')
        f5.write('new project')
