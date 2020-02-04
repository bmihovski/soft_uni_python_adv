def find_elem(target, find_char):
    rows = len(target)
    for row in range(rows):
        line = target[row]
        if symbol in line:
            return row, line.index(find_char)
    return None


def input_user_data():
    size = int(input())
    return [input() for _ in range(size)], input()


matrix, symbol = input_user_data()
result = find_elem(matrix, symbol)
if result:
    x, y = result
    print(f"({x}, {y})")
else:
    print(f"{symbol} does not occur in the matrix")
