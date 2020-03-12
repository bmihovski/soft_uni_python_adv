def number_increment(numbers):
    def increase():
        new_nums = list(map(lambda num: num + 1, numbers))
        return new_nums
    return increase()


from unittest import TestCase


class NumbersIncrement(TestCase):
    def test_zero(self):
        self.assertEqual([2, 3, 4], number_increment([1, 2, 3]))
