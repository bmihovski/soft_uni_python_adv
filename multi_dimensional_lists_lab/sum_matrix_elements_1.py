def read_from_sdin():
    rows, columns = list(map(int, input().split(", ")))
    matrix = []
    for row in range(rows):
        matrix.append(0)
        line = list(map(int, input().split(", ")))
        matrix[row] = line
    return matrix


matrix_to_read = read_from_sdin()
sum_rows = [sum(el) for el in matrix_to_read]

print(sum(sum_rows))
print(matrix_to_read)
