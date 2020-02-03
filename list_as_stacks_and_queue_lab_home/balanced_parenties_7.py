from collections import deque

pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
}


def find_balanced(exp):
    sequence_chars = deque()
    valid = True
    if 2 <= len(exp) <= 1000:
        for char in exp:
            if char in "({[":
                sequence_chars.append(char)
            elif char in "})]":
                if sequence_chars:
                    current = sequence_chars[-1]
                    if pairs[current] == char:
                        sequence_chars.pop()
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break

        if valid:
            print("YES")
        else:
            print("NO")


expression_input = input()
find_balanced(expression_input)
