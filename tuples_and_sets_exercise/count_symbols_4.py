def solve(sentence):
    occurrence = dict()
    for letter in sentence:
        if letter not in occurrence:
            occurrence[letter] = 1
        else:
            occurrence[letter] += 1
    return occurrence


word = input()
result = solve(word)
{print(f"{letter}: {occur} time/s") for letter, occur in sorted(result.items())}
