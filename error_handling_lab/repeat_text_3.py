def multiply_text(word_to_multi, number):
    try:
        if not number.isdigit():
            raise TypeError("Variable times must be an integer")
        print(word_to_multi * int(number))
    except TypeError as error:
        print(error)


word = input()
multiplier = input()
multiply_text(word, multiplier)
