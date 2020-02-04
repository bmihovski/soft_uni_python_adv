def solve():
    initial_reservations = set()
    checked_in = set()
    is_checked = False
    while True:
        input_data = input()
        if input_data == "END":
            break
        if input_data == "PARTY":
            is_checked = True
        if is_checked:
            checked_in.add(input_data)
        initial_reservations.add(input_data)
    if checked_in:
        final_guests = initial_reservations.symmetric_difference(checked_in)
        print(len(final_guests))
        [print(el) for el in sorted(final_guests)]


solve()
