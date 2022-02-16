from functools import wraps


def val_checker(called_function):
    def internal_function(func):
        @wraps(func)
        def hidden_calc_cube(x):
            if not called_function(x):
                raise ValueError(f'wrong val {x}')
            return func(x)

        return hidden_calc_cube

    return internal_function


def сhecking_the_integrity_of_numbers(x):
    if type(x) == int and x >= 0:
        return True
    return False


@val_checker(сhecking_the_integrity_of_numbers)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    # print(calc_cube(5))
    print(calc_cube('ss'))
