math_oper = {
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '^': lambda x, y: x ** y,
}


def calc_func(operation):
    return math_oper[operation]
