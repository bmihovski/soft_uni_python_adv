input_count = int(input())

matrix = [list(map(int, input().split(", "))) for _ in range(input_count)]

print([num for sublist in matrix for num in sublist])
