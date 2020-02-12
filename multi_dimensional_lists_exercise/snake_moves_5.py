from collections import deque

input_rows, input_cols = tuple(filter(lambda x: 1 <= x <= 12, map(int, input().split())))
input_snake = deque(input())


def print_snake(check_rows, check_cols, check_snake):
    matrix = list()

    for row in range(check_rows):
        matrix.append(["" for _ in range(check_cols)])
        for col in range(check_cols):
            if row % 2 == 0:
                element = input_snake.popleft()
                matrix[row][col] = element
                check_snake.append(element)
            else:
                element = input_snake.popleft()
                matrix[row][(check_cols - col) - 1] = element
                check_snake.append(element)

    return matrix


print_matrix = print_snake(input_rows, input_cols, input_snake)
[print(''.join(map(str, el))) for el in print_matrix]
