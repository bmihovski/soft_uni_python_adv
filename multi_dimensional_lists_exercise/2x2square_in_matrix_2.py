matrix_rows_input, matrix_cols_in = map(int, input().split())
matrix_input = [list(input().split()) for _ in range(matrix_rows_input)]


def find_matches(matrix, matrix_rows, matrix_cols):
    match = 0
    for row in range(matrix_rows - 1):
        for col in range(matrix_cols - 1):
            current_sum = matrix[row][col] + \
                         matrix[row][col + 1] + \
                         matrix[row + 1][col] + \
                         matrix[row + 1][col + 1]
            if current_sum == 4 * matrix[row][col]:
                match += 1
    return match


print(find_matches(matrix_input, matrix_rows_input, matrix_cols_in))
