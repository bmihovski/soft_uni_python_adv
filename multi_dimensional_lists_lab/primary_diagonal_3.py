def find_primary_diag(matrix):
    rows = len(matrix)
    sum_diag = 0
    for row in range(rows):
        sum_diag += matrix[row][row]
    return sum_diag


def user_input():
    rows = int(input())
    return [list(map(int, input().split())) for _ in range(rows)]


matrix = user_input()
print(find_primary_diag(matrix))
