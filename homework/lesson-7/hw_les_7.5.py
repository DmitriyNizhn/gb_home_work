import os
import json
from collections import defaultdict

root_dir = 'some_data'
file_size = defaultdict(list)
count = 0
for root, dirs, files in os.walk(root_dir):
    for file in files:
        f_path = os.path.join(root, file)
        size = os.stat(f_path).st_size
        key = 10 ** (len(str(size)) - 1)
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        file_size[key].append(ext)

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(file_size, f, ensure_ascii=False, indent=4)

with open('summary.json', 'r', encoding='utf-8') as f:
    load_dict = f.read()
    my_dict = json.loads(load_dict)

for key, ext in sorted(my_dict.items(),
                       key=lambda x: len(x[1]), reverse=False):
    print(f'    {key}: ({len(ext)}, {list(set(ext))}),')
