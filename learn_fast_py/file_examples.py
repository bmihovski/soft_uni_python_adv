#!/usr/bin/env python3

with open("text.txt", "w") as test_file:
    test_file.write("tester")

with open("text.txt", "a") as append_file:
    append_file.write("\nmore text")

with open("text.txt", "r") as content:
    print(content.read())
