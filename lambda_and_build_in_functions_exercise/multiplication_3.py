multiply_index = int(input())
user_input = map(int, input().split())
print(*(map(lambda x: x * multiply_index, user_input)))
