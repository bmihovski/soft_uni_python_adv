def read_number(nums):
    phone_book = dict()
    for record in nums:
        name, number = record.split("-")
        if name not in phone_book:
            phone_book[name] = number
        else:
            phone_book[name] = number
    return phone_book


def collect_numbers():
    collected_nums = list()
    while True:
        user_input = input()
        if user_input == "search":
            break
        else:
            collected_nums.append(user_input)
    return collected_nums


def search_number(result_dict):
    while True:
        user_input = input()
        if user_input == "stop":
            break
        elif user_input in result_dict:
            print(f"{user_input} -> {result_dict.get(user_input)}")
        else:
            print(f"Contact {user_input} does not exist.")


numbers = collect_numbers()
result = read_number(numbers)
search_number(result)
