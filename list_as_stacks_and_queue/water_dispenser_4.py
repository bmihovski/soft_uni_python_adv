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
        person = clients.popleft()
        person_liters = int(input())
        if person_liters >= liters:
            print(f'{person} got water')
            liters -= int(user_input)
        else:
            print(f'{person} must wait')
    if user_input.startswith("refill"):
        liters_to_refill = int(user_input.split())
        liters += liters_to_refill
        print(f'{liters} liters left')

dispence()
