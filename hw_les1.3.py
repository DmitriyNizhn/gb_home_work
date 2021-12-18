for i in range(1, 101):
    if i != 11 and i % 10 == 1:
        print(i, 'процент')
    elif (i % 10 > 4 and i % 10 < 10) or i % 10 == 0 or i // 10 == 1:
        print(i, 'процентов')
    else:
        print(i, 'процента')
