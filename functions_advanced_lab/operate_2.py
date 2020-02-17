from functools import reduce


def operate(operator, *args):
    op = {"+": lambda x, y: x + y,
          "*": lambda x, y: x * y,
          "-": lambda x, y: x - y,
          "/": lambda x, y: x / y,
          "%": lambda x, y: x % y,
          }

    return reduce(op[operator], args)

