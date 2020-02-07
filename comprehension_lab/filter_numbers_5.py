start, end = [int(input()) for _ in range(2)]


def is_valid(x):
    min_val = 2
    max_val = 10
    return [x for el in range(min_val, max_val + 1) if x % el == 0]


print([x for x in range(start, end + 1) if is_valid(x)])
