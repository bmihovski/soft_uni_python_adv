def best_matrix(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    best_result = None
    best_sum = None
    for row in range(row_count - 1):
        for col in range(col_count - 1):
            current_sum = matrix[row][col] + \
                          matrix[row][col + 1] + \
                          matrix[row + 1][col] + \
                          matrix[row + 1][col + 1]

            if best_sum:
                if best_sum < current_sum:
                    best_sum = current_sum
                    best_result = row, col
            else:
                best_sum = current_sum
                best_result = row, col

    best_result_mtrx_start_x = best_result[0]
    best_result_mtrx_stop_x = best_result[1]

    result_matrix = [
        [matrix[best_result_mtrx_start_x][best_result_mtrx_stop_x],
            matrix[best_result_mtrx_start_x][best_result_mtrx_stop_x + 1]],
        [matrix[best_result_mtrx_start_x + 1][best_result_mtrx_stop_x],
            matrix[best_result_mtrx_start_x + 1][best_result_mtrx_stop_x + 1]],
    ]

    return best_sum, result_matrix


def get_inputs():
    rows_count, _ = list(map(int, input().split(", ")))
    return [list(map(int, input().split(", "))) for _ in range(rows_count)]


inp_matrix = get_inputs()
mtrx_sum, mtrx_best_result = best_matrix(inp_matrix)
[print(' '.join(map(str, el))) for el in mtrx_best_result]
print(mtrx_sum)
