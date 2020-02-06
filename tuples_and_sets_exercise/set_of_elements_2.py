first_set_len, second_set_len = tuple(map(int, input().split()))

first_set = {int(input()) for _ in range(first_set_len)}
second_set = {int(input()) for _ in range(second_set_len)}

[print(el) for el in first_set.intersection(second_set)]
