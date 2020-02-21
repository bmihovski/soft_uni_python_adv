nums_input = list(map(int, input().split()))

negative_nums = filter(lambda x: x < 0, nums_input)
positive_nums = filter(lambda x: x >= 0, nums_input)
sum_of_negatives = sum(negative_nums)
sum_of_positives = sum(positive_nums)

print(sum_of_negatives)
print(sum_of_positives)
if abs(sum_of_negatives) > sum_of_positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
