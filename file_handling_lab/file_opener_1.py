try:
    open("../08-File-Handling-Lab-Resources/text.txt", 'r')
    print("File found")
except FileNotFoundError as e:
    print("File not found")
