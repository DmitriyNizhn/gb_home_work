class OwnError(Exception):
    pass


a = input('Введите число: ')
my_list = []
while a != 'stop':
    try:
        if not a.isdigit():
            raise OwnError('Введите именно число')
    except OwnError as err:
        print(err)
    else:
        a = int(a)
        my_list.append(a)
    a = input('Введите "stop" для завершления ввода: ')
print(my_list)
