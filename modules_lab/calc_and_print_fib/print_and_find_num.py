def results_find_and_print(*args):
    if len(args) == 1:
        print(*args[0])
    elif args[1] in args[0]:
        print(f"The number - {args[1]} is at index {args[0].index(args[1])}")
    else:
        print(f"The number {args[1]} is not in the sequence")
