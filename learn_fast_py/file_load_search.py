while True:
    try:
        file_to_open = input("Enter file to open: ")
        with open(file_to_open) as target:
            content = target.read()
            print(content)
            break
    except FileNotFoundError:
        print("This file not fount try with another one")
