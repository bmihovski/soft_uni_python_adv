def read_matrix_values():
    matrix_rows, matrix_columns = map(int, input().split())
    matrix = [input().split() for _ in range(matrix_rows)]
    while True:
        user_command = input()
        if user_command == "END":
            break
        if not user_command.startswith("swap"):
            print("Invalid input!")
            continue
        try:
            row1, col1, row2, col2 = tuple(map(int, user_command[5:].split()))
        except ValueError:
            print("Invalid input!")
            continue
        try:
            first_swap = matrix[row1][col1]
            second_swap = matrix[row2][col2]
            matrix[row1][col1] = second_swap
            matrix[row2][col2] = first_swap
            [print(' '.join(map(str, matrix[row]))) for row in range(matrix_rows)]
        except IndexError:
            print("Invalid input!")
            continue


read_matrix_values()
