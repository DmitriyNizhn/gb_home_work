coub_list = []  # список нечетных чисел, в кубе
for i in range(1, 1000):
    if i % 2 != 0:
        i = i ** 3
        coub_list.append(i)
sum_my_num = 0  # Сумма необходимых чисел
for i in coub_list:
    i = i + 17  # к каждому числу списка добавили 17
    length = len(str(i))
    sum_i_num = 0  # Сумма чисел состовляющих i число
    copy_i = i # Создаем копию, что бы не изменять i
    while True:
        sum_i_num += copy_i % 10
        copy_i //= 10
        length -= 1
        if length == 0:
            break
    if sum_i_num % 7 == 0:
        sum_my_num += i
print(sum_my_num)
