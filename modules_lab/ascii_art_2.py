from pyfiglet import figlet_format


def print_art(word):
    return figlet_format(word)


print(print_art(input()))
