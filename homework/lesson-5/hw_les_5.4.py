from time import perf_counter


def more_last_num(*src):
    result = []
    last_num = src[0]
    for i in src:
        if i > last_num:
            result.append(i)
        last_num = i
    return result


def more_last_num_gen(*src):
    last_num = src[0]
    for i in src:
        if i > last_num:
            yield i
        last_num = i


# Примерно одинаковая скорость, генератор из 2-х выигрывает
start = perf_counter()
print(more_last_num(300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55))
print(1, (perf_counter() - start) * 10 ** 5)
start = perf_counter()
print(*more_last_num_gen(300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55))
print(2, (perf_counter() - start) * 10 ** 5)

# Быстрее всего через List Comprehensions
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
nums = [src[i] for i in range(1, len(src) - 1) if src[i] > src[i - 1]]
print(nums)
print(3, (perf_counter() - start) * 10 ** 5)

# генератор не выигрывает по времени, так еще и нужно будет избавляться от первого элемента
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
last_num = src[0]
nums = (src[i] for i in range(0, len(src) - 1) if src[i] > src[i - 1])
print(*nums)
print(4, (perf_counter() - start) * 10 ** 5)
