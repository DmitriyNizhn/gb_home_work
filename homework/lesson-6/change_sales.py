import sys
import os

num_line = int(sys.argv[1])
new_price = sys.argv[2]
count_line = 0
with open('bakery.csv', 'r+', encoding='utf-8') as file1, \
        open('new_bakery.txt', 'w', encoding='utf-8') as file2:
    for line in file1:
        count_line += 1
        if num_line == count_line:
            file2.write(new_price + '\n')
        else:
            file2.write(line)

if count_line < num_line:
    print("Такого номера записи еще не существует")

os.remove('bakery.csv')
os.rename('new_bakery.txt', 'bakery.csv')
