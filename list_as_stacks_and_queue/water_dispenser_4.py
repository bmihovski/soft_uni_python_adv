from collections import deque


def dispence():
    clients = deque()
    liters = 0
    user_input_liters = int(input())
    liters += user_input_liters

    while True:
        user_input = input()
        if user_input == "Start":
            break
        clients.append(user_input)
    while clients:
        command = input()
        if command.startswith("refill"):
            liters += int(command.split()[1])
            continue
        person = clients.popleft()
        person_liters = int(command)
        if liters < person_liters:
            print(f'{person} must wait')
        else:
            liters -= person_liters
            print(f'{person} got water')

    print(f'{liters} liters left')

dispence()
