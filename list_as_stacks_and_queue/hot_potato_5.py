from collections import deque


def potato(people, n):
    players = deque(people)

    index = 0
    while players:
        user_to_remove = players.popleft()
        index += 1
        if index == n:
            index = 0
            if players:
                print(f"Removed {user_to_remove}")
                n = n % len(players)
                if n == 0:
                    n = len(players)
            else:
                print(f"Last is {user_to_remove}")
        else:
            players.append(user_to_remove)


potato(input().split(), int(input()))
