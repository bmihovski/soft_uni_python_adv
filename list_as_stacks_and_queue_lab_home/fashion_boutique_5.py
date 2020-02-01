from collections import deque


def shop_storage():
    boxes = deque()
    total = 0
    sum_vals = []
    input_boxes = list(map(int, input().split()))
    capacity = int(input())
    [boxes.appendleft(int(box)) for box in input_boxes if 0 <= box <= 20 and box <= capacity and 0 <= capacity <= 20]

    while boxes:
        single_box = boxes.popleft()
        sum_vals.append(single_box)
        if capacity == sum(sum_vals):
            total += 1
            sum_vals = []
        elif capacity > sum(sum_vals) and boxes:
            continue
        elif capacity < sum(sum_vals):
            boxes.appendleft(single_box)
            total += 1
            sum_vals = []
        else:
            total += 1
            break

    return print(total)


shop_storage()
