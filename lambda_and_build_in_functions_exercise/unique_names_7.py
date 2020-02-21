names_input = input().split()

filter_names = filter(lambda x: x.istitle(), names_input)

print(sum(map(lambda x: len(x), list(filter_names))))
