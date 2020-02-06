def get_by_row(inter):
    first_intercept, second_interception = inter.split("-")
    first_start, first_end = map(int, first_intercept.split(","))
    second_start, second_end = map(int, second_interception.split(","))
    first_set = {el for el in range(first_start, first_end + 1)}
    second_set = {el for el in range(second_start, second_end + 1)}

    return first_set.intersection(second_set)


def get_inter_by_len(intersect):
    long_interceptintion = set()
    for inter in intersect:
        current_inter = get_by_row(inter)
        if len(long_interceptintion) < len(current_inter):
            long_interceptintion = current_inter
    return long_interceptintion


input_nums = int(input())
intersection = [input() for _ in range(input_nums)]

longest_interception = get_inter_by_len(intersection)
print(f"Longest intersection is {list(longest_interception)} with length {len(longest_interception)}")
