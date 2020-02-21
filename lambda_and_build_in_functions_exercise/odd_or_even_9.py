user_command = input()
nums_input = list(map(int, input().split()))

even_nums = filter(lambda x: x % 2 == 0, nums_input)
odd_nums = filter(lambda x: x % 2 == 1, nums_input)

command = {
    "Odd": sum(odd_nums) * len(nums_input),
    "Even": sum(even_nums) * len(nums_input),
}

print(command[user_command])
