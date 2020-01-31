from collections import deque


def ops():
    test_stack = deque()
    num_queries = 0
    total_ops = int(input())
    if 1 <= total_ops <= 105:
        num_queries = total_ops
    index = 0
    while True:
        if num_queries == index:
            print(", ".join(map(str, test_stack)))
            break
        index += 1
        [*values] = input().split()
        if len(values) == 2 and int(values[0]) == 1 and 1 <= int(values[1]) <= 109:
            test_stack.appendleft(int(values[1]))
            continue
        elif int(values[0]) == 2 and test_stack:
            test_stack.popleft()
            continue
        elif int(values[0]) == 3 and test_stack:
            print(max(test_stack))
            continue
        elif int(values[0]) == 4 and test_stack:
            print(min(test_stack))
            continue


ops()
