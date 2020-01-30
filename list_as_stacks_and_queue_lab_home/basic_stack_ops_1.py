from collections import deque


first_inps = []
stack_els = deque()
[first_inps.append(int(el)) for el in input().split()]
_, to_pop, to_check = first_inps

[stack_els.append(int(el)) for el in input().split()]

[stack_els.pop() for _ in range(to_pop)]

if to_check in stack_els:
    print(True)
elif not stack_els:
    print(0)
else:
    print(min(stack_els))
