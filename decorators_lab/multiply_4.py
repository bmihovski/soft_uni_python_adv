def multiply(times):
    def decorator(function):
        def wrapper(num):
            result = function(num) * times
            return result
        return wrapper
    return decorator


from unittest import TestCase


class MultiplyTests(TestCase):
    def test_zero(self):
        @multiply(3)
        def add_ten(number):
            return number + 10
        self.assertEqual(39, add_ten(3))
