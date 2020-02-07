count_matrix = int(input())
matrix = [map(int, input().split(", ")) for _ in range(count_matrix)]
print([[x for x in el if x % 2 == 0] for el in matrix])
