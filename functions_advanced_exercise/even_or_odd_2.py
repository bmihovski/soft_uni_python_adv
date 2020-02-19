def even_odd(*args):
    command = {"even":
              lambda x: x % 2 == 0,
               "odd":
              lambda x: x % 2 == 1
               }

    return list(filter(command[args[-1]], args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
