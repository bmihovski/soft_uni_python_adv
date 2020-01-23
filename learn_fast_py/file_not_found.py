try:
    with open("fsff.txt") as test_file:
        content = test_file.read()
except FileNotFoundError:
    print("Error try with another file")
