from functools import wraps


def val_checker(arg):
    def type_arg(func):
        @wraps(func)
        def wraper(*args):
            for el in args:
                if arg(el):
                    continue
                else:
                    msg = f'ValueError: wrong val {args}'
                    raise ValueError(msg)
            answer = func(*args)
            return tuple(answer)

        return wraper

    return type_arg


@val_checker(lambda x: x > 0)
def calc_cube(*num):
    '''calculate the number in the cube'''
    return (el ** 3 for el in num)


print(calc_cube(3, 4, 5))

