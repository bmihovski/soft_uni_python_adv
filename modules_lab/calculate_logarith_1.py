from math import log


def calc_log(num_to_calc, base_num):
    result = 0
    if base_num == "natural":
        result = log(num_to_calc)
    else:
        result = log(num_to_calc, int(base_num))
    return result


num = int(input())
base = input()
print(f"{round(calc_log(num, base), 2):.2f}")
