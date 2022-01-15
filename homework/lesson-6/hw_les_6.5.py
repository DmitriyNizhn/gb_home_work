import sys
import os

users_file = sys.argv[1]
hobby_file = sys.argv[2]
new_file = sys.argv[3]

if os.stat(users_file).st_size < os.stat(hobby_file).st_size:
    sys.exit(1)
else:
    with open(users_file, encoding='utf-8') as file1, \
            open(hobby_file, encoding='utf-8') as file2, \
            open(new_file, 'w', encoding='utf-8') as file3:
        for name in file1:
            hobby = file2.readline().strip('\n')
            if not hobby:
                hobby = 'None'
            file3.write(f'{name.strip()}: {hobby}\n')
