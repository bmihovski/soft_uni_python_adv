names_input = input().split()

filter_names = filter(lambda x: x[0].isupper() and x[1:].islower(), names_input)

print(sum(map(lambda x: len(x), list(filter_names))))
