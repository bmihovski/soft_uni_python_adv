def calc_fib(num):
    fibonacci_numbers = [0, 1]
    for i in range(2, num):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers

