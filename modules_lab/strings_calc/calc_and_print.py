from strings_calc.return_calc_func import calc_func


def calc_stings(calc_str):
    num1, oper, num2 = calc_str.split()
    print(f"{calc_func(oper)(float(num1), int(num2)):.2f}")
