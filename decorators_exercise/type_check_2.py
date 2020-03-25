def type_check(arg_type):
    def decorator(func):
        def wrapper(arg):
            current_type = type(arg).__name__
            if arg_type.__name__ != current_type:
                return "Bad Type"
            return func(arg)
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))

from unittest import TestCase


class TypeCheck(TestCase):
    def test_int(self):
        @type_check(int)
        def times2(num):
            return num*2
        self.assertEqual(4, times2(2))
        self.assertEqual("Bad Type", times2('Not A Number'))

    def test_str(self):
        @type_check(str)
        def first_letter(word):
            return word[0]
        self.assertEqual("H", first_letter('Hello World'))
        self.assertEqual("Bad Type", first_letter(['Not', 'A', 'String']))
