user_input = map(float, input().split())
nums_round = list(map(round, user_input))
multiplied_by_3 = map(lambda x: x * 3, nums_round)
print(min(nums_round))
print(max(nums_round))
print(*sorted(set(multiplied_by_3)))