from collections import deque


def supermarket():
    clients = deque()

    while True:
        enter_client = input()

        if enter_client == "Paid":
            while clients:
                print(clients.popleft())
        else:
            clients.append(enter_client)
        if enter_client == "End":
            clients.popleft()
            print(f"{len(clients)} people remaining.")
            break

supermarket()
