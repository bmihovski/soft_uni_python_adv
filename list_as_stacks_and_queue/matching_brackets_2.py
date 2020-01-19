def find_expression(expr):
    proc_expression = []
    start_pos = 0
    end_pos = 0
    start_indexes = []

    for pos in range(len(expr)):
        if expr[pos] == "(":
            start_indexes.append(pos)
        elif expr[pos] == ")":
            start_pos = start_indexes.pop()
            end_pos = pos
            proc_expression.append(expr[start_pos:end_pos + 1])
    return proc_expression


expression_input = input()

[print(exp) for exp in find_expression(expression_input)]
