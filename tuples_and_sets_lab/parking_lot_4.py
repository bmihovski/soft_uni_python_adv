def solve():
    parking_lot = set()
    while True:
        [*input_data] = input().split(", ")
        if input_data[0] == "END":
            break
        elif input_data[0] == "IN":
            parking_lot.add(input_data[1])
        elif input_data[0] == "OUT" and parking_lot:
            parking_lot.remove(input_data[1])
    if parking_lot:
        [print(el) for el in parking_lot]
    else:
        print("Parking Lot is Empty")


solve()
