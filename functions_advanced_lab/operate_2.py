from functools import reduce


def operate(operator, *args):
    op = {"+": lambda x, y: x + y,
          "*": lambda x, y: x * y,
          "-": lambda x, y: x - y,
          "/": lambda x, y: x / y,
          "%": lambda x, y: x % y,
          }

    return reduce(op[operator], args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
