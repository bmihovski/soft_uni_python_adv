from collections import deque


first_inputs = []
infos_to_process = deque()

[first_inputs.append(int(el)) for el in input().split()]

[infos_to_process.append(int(el)) for el in input().split()]

_, item_to_remove, value_to_check = first_inputs

[infos_to_process.popleft() for _ in range(item_to_remove)]

if value_to_check in infos_to_process:
    print(True)
elif not infos_to_process:
    print(0)
else:
    print(min(infos_to_process))
