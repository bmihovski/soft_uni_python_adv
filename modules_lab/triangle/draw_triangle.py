from triangle.print_triangle_row import print_row


def print_triangle(size):
    for row in range(size + 1):
        print_row(row)
    for row in range(size - 1, -1, -1):
        print_row(row)
