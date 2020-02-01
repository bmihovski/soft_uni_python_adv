from collections import deque


def fast_food():
    total_food = int(input())
    if 0 <= total_food <= 1000:
        orders = deque()
        [orders.append(int(el)) for el in input().split()]

        print(max(orders))
        while orders:
            order = orders.popleft()
            if order < total_food and orders:
                total_food -= order
            elif order > total_food:
                orders.appendleft(order)
                print(f"Orders left: {' '.join(map(str, orders))}")
                break

        if not orders:
            print("Orders complete")


fast_food()
