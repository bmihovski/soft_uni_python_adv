user_input = map(int, input().split())
only_negative = filter(lambda x: x < 0, user_input)
sum_negative = sum(only_negative)

print(abs(sum_negative))
