user_input = input().split()
get_only_digits = filter(lambda x: x.isdigit(), user_input)
get_only_more_than_length = filter(lambda y: int(y) > len(user_input), get_only_digits)
result = sorted(map(int, get_only_more_than_length))

print(*result)
