def get_matrix_sum(check_matrix, diment):
    first_diagonal = [check_matrix[el][el] for el in range(diment)]
    print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
    second_diagonal = [check_matrix[el][(diment - 1) - el] for el in range(diment)]
    print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")


matrix_dimensions = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(matrix_dimensions)]
get_matrix_sum(matrix, matrix_dimensions)
