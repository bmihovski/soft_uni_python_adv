count_of_el = int(input())
final_elems = set()
[{final_elems.add(el) for el in input().split()} for _ in range(count_of_el)]

[print(el) for el in final_elems]
