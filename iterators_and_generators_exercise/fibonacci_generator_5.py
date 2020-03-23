def fibonacci():
    first_num = 0
    second_num = 1
    yield first_num
    yield second_num

    while True:
        next_number = first_num + second_num
        yield next_number
        first_num = second_num
        second_num = next_number
