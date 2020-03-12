def even_numbers(function):
    def wrapper(numbers):
        odd_numbers = list(filter(lambda num: num % 2 == 0, numbers))
        return odd_numbers
    return wrapper


from unittest import TestCase


class EvenNumbersTests(TestCase):
    def test_zero(self):
        @even_numbers
        def get_numbers(numbers):
            return numbers
        self.assertEqual([2, 4], get_numbers([1, 2, 3, 4, 5]))
