def solve(values):
    collect_val = dict()
    for value in values:
        if value not in collect_val:
            collect_val[value] = 0
        collect_val[value] += 1
    for numb, count in collect_val.items():
        print(f"{numb} - {count} times")


input_vals = list(map(float, input().split()))
solve(input_vals)

