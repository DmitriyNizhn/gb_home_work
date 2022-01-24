from functools import wraps


def type_arg(func):
    @wraps(func)
    def wraper(*args):
        type_num = [f'{func.__name__}']
        for el in args:
            type_num.append(f'({el}: {type(el)})')
        print(tuple(type_num))
        answer = func(*args)
        return tuple(answer)

    return wraper


@type_arg
def calc_cube(*num):
    '''calculate the number in the cube'''
    return (el ** 3 for el in num)


print(calc_cube(9, 8))
help(calc_cube)
