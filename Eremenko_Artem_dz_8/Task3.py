from functools import wraps


def type_logger(func):
    @wraps(func)
    def func_in(*elem):
        result = [func(el) for el in elem]
        str_out = ''
        for i in range(len(result)):
            str_in_func = f'{func.__name__}({elem[i]}: {type(result[i])})'
            str_in_func = str_in_func.strip()
            if i < len(result) - 1:
                str_out += f'{str_in_func}, '
            else:
                str_out += str_in_func
        return str_out

    return func_in


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 6, 7))
