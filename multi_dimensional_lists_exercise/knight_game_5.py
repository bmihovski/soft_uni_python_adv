table_count = int(input())
chests_to_check = [[x for x in input()] for _ in range(table_count)]


def get_damage(row, col, matrix):
    counter = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == "K":
            counter += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == "K":
            counter += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == "K":
            counter += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == "K":
            counter += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == "K":
            counter += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == "K":
            counter += 1

    return counter


def check_knight(count, matrix):
    knight_pos = list()
    deleted_knights = 0
    while True:
        max_damage = 0
        for row in range(count):
            for col in range(count):
                if matrix[row][col] == "K":
                    current_damage = get_damage(row, col, matrix)
                    if current_damage > max_damage:
                        max_damage = current_damage
                        knight_pos = [row, col]

        if max_damage == 0:
            break
        matrix[knight_pos[0]][knight_pos[1]] = "O"
        deleted_knights += 1
        knight_pos = []
    return deleted_knights


knight_to_remove = check_knight(table_count, chests_to_check)
print(knight_to_remove)
