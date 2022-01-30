class OwnError(Exception):
    pass


in_num = input('Введите делитель')

try:
    in_num = int(in_num)
    if in_num == 0:
        raise OwnError('Делить на 0 нельзя')
except (ValueError, OwnError) as err:
    print(err)
else:
    answ = 100 / in_num
    print(answ)
