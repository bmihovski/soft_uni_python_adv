num_names = int(input())

unique_names = {input() for _ in range(num_names)}
[print(name) for name in unique_names]
