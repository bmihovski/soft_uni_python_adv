def get_combinations(values, index, display_it):
    if len(values) == index:
        display_it(values)
        return

    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        get_combinations(values, index + 1, display_it)
        values[i], values[index] = values[index], values[i]


def format_it(values):
    return ''.join(values)


get_combinations(list(input()), 0, lambda x: print(format_it(x)))
