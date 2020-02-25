from calc_and_print_fib.calc_fib import calc_fib
from calc_and_print_fib.print_and_find_num import results_find_and_print


def solve():
    fib_nums = []
    while True:
        user_input = input().split()
        if user_input[0] == "Stop":
            break
        value_to_check_or_gen = int(user_input[-1])
        if user_input[0] == "Create":
            fib_nums = calc_fib(value_to_check_or_gen)
            results_find_and_print(fib_nums)
            continue
        else:
            results_find_and_print(fib_nums, value_to_check_or_gen)
            continue


solve()
