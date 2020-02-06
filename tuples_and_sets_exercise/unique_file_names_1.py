num_lines = int(input())
names = {input() for el in range(num_lines)}

[print(name) for name in names]
