def palindrome(word_to_check, start):
    second_idx = len(word_to_check) - 1 - start
    if start == len(word_to_check) // 2:
        return f"{word_to_check} is a palindrome"

    if word_to_check[start] == word_to_check[second_idx]:
        return palindrome(word_to_check, start + 1)
    else:
        return f"{word_to_check} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("rater", 0))
