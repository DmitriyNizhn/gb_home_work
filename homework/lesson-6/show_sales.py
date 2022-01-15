import sys

with open('bakery.csv', encoding='utf-8') as file:
    if len(sys.argv) == 2:
        start_line = int(sys.argv[1])
        lines = file.readlines()
        lines = ''.join(lines[start_line:])
        print(lines)
    elif len(sys.argv) > 2:
        start_line = int(sys.argv[1])
        finish_line = int(sys.argv[2])
        lines = file.readlines()
        lines = ''.join(lines[start_line:finish_line + 1])
        print(lines)
    else:
        lines = file.read()
        print(lines.strip())
