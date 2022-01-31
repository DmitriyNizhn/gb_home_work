import os
from collections import defaultdict

root_dir = 'some_data'
file_size = defaultdict(list)
count = 0
for file in os.scandir(root_dir):
    size = (os.stat(file).st_size)
    key = 10 ** (len(str(size)) - 1)
    count += 1
    file_size[key].append(count)

for key, count in sorted(file_size.items(),
                         key=lambda x: len(x[1]), reverse=False):
    print(key, len(count))
