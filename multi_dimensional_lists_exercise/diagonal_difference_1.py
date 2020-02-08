matrix_size = int(input())

matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

primary_diagonal = 0
secondary_diagonal = 0

for index in range(matrix_size):
    primary_diagonal += matrix[index][index]
    secondary_diagonal += matrix[index][(matrix_size - 1) - index]

print(abs(primary_diagonal - secondary_diagonal))
