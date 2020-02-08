def calculate_sum(matrix, rows_count, column_count):
    max_sum = 0
    max_matrix = []
    for row in range(rows_count):
        for col in range(column_count):
            try:
                sum_3_3 = matrix[row][col] + \
                          matrix[row][col + 1] + \
                          matrix[row][col + 2] + \
                          matrix[row + 1][col] + \
                          matrix[row + 1][col + 1] + \
                          matrix[row + 1][col + 2] + \
                          matrix[row + 2][col] + \
                          matrix[row + 2][col + 1] + \
                          matrix[row + 2][col + 2]
                if max_sum < sum_3_3:
                    max_sum = sum_3_3
                    first_row = f"{matrix[row][col]} {matrix[row][col + 1]} {matrix[row][col + 2]}"
                    second_row = f"{matrix[row + 1][col]} {matrix[row + 1][col + 1]} {matrix[row + 1][col + 2]}"
                    third_row = f"{matrix[row + 2][col]} {matrix[row + 2][col + 1]} {matrix[row + 2][col + 2]}"
                    max_matrix = [first_row, second_row, third_row]
            except IndexError:
                continue
    return max_sum, max_matrix


matrix_rows_count, matrix_cols_count = map(int, input().split())
matrix_input = [list(map(int, input().split())) for _ in range(matrix_rows_count)]

el_sum, max_martx = calculate_sum(matrix_input, matrix_rows_count, matrix_cols_count)

print(f"Sum = {el_sum}")
[print(row) for row in max_martx]
