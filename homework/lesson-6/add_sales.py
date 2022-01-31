import sys, os

with open('bakery.csv', 'a+', encoding='utf-8') as file:
    file.write(sys.argv[1] + '\n')
