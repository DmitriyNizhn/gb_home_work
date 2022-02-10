def odd_num(n):
    for i in range(1, n + 1, 2):
        yield i


nums = odd_num(15)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
