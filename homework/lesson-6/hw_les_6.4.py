import os
import sys


if os.stat('users.txt').st_size < os.stat('hobby.txt').st_size:
    sys.exit(1)
else:
    with open('users.txt', encoding='utf-8') as file1, \
            open('hobby.txt', encoding='utf-8') as file2, \
            open('users_hobby.txt', 'w', encoding='utf-8') as file3:
        #     users_hobby = {}
        #     for name in file1:
        #         users_hobby[name.strip()] = None
        #     keys = list(users_hobby.keys())
        #     i = 0
        #     for hobby in file2:
        #         users_hobby[keys[i]] = hobby.strip()
        #         i += 1
        #     for keys, value in users_hobby.items():
        #         file3.write(f'{keys}: {value} \n')
        for name in file1:
            hobby = file2.readline().strip('\n')
            if not hobby:
                hobby = 'None'
            file3.write(f'{name.strip()}: {hobby}\n')
