import json
import sys

with open('users.txt', encoding='utf-8') as f1, \
        open('hobby.txt', encoding='utf-8') as f2, \
        open('hobby_dict.json', 'w', encoding='utf-8') as f3:
    names_content = (f1.read()).splitlines()
    hobby_content = (f2.read()).splitlines()
    if len(names_content) > len(hobby_content):
        hobby_dict = dict.fromkeys(names_content) | dict(zip(names_content, hobby_content))
        json.dump(hobby_dict, f3, ensure_ascii=False, indent=4)
    else:
        sys.exit(1)
print(type(names_content))
