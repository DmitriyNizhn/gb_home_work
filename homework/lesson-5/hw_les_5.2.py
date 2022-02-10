n = 15
nums_gen = (num for num in range(1, n + 1) if num % 2 != 0)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(*nums_gen)
