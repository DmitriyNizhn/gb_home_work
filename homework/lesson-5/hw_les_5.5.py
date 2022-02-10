# Нужно дальше оптимизировать

from random import randint
from time import perf_counter


def unic_num(src):
    unic_list = []
    re_list = []
    for i in src:
        if i in unic_list:
            unic_list.remove(i)
            re_list.append(i)
        else:
            if i in re_list:
                continue
            else:
                unic_list.append(i)
    return unic_list


def my_list(n):
    result = []
    while n != 0:
        result.append(randint(1, 1000))
        n -= 1
    return result


src = my_list(1000)
start = perf_counter()
print(unic_num(src))
print(1, perf_counter() - start)

src = my_list(1000)
start = perf_counter()
only_one_num = [el for el in src if src.count(el) < 2]
print(only_one_num)
print(2, perf_counter() - start)

src = my_list(1000)
start = perf_counter()
uni_nums = set()
tmp = set()
for el in src:
    if el not in tmp:
        uni_nums.add(el)
    else:
        uni_nums.discard(el)
    tmp.add(el)
uni_nums_ord = [el for el in src if el in uni_nums]
print(uni_nums_ord)
print(3, perf_counter() - start)
