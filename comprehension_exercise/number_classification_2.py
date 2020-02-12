def get_numbers_classification(nums):
    print("Positive: " + ", ".join([str(num) for num in nums if num >= 0]))
    print("Negative: " + ", ".join([str(num) for num in nums if num < 0]))
    print("Even: " + ", ".join([str(num) for num in nums if num % 2 == 0]))
    print("Odd: " + ", ".join([str(num) for num in nums if num % 2 == 1]))


get_numbers_classification(list(map(int, input().split(", "))))
