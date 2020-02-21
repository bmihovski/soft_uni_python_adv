user_input = list(map(float, input().split()))

floats_round = map(round, user_input)
floats_calc = map(lambda x: x * len(user_input), floats_round)

print(sum(floats_calc))
