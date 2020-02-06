input_data = input()
vovels = ['a', 'o', 'u', 'e', 'i']
result = [x for x in input_data if x.lower() not in vovels]
print(''.join(result))
