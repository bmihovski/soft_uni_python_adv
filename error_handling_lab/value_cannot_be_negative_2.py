class ValueCannotBeNegative(Exception):
    pass


def check_value():
    for _ in range(5):
        user_value = int(input())
        if user_value < 0:
            raise ValueCannotBeNegative
        print(user_value)


class TestClass(ValueCannotBeNegative):

    check_value()
