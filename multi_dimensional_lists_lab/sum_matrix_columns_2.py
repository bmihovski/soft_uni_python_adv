def get_user_data():
    (rows, columns) = map(int, input().split(", "))

    return [list(map(int, input().split(' '))) for _ in range(rows)]


def sum_colums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums_col = [0] * cols
    for row in range(rows):
        for col in range(cols):
            sums_col[col] += matrix[row][col]
    return sums_col


data = get_user_data()
[print(el) for el in sum_colums(data)]
