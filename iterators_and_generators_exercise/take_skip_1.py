class take_skip:
    __initial_result = 0

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        else:
            self.count -= 1
            self.__initial_result += self.step
            return self.__initial_result - self.step


from unittest import TestCase


class TakeSkipTests(TestCase):
    def test_zero(self):
        numbers = take_skip(2, 6)
        self.assertEqual([0, 2, 4, 6, 8, 10], list(numbers))

    def test_one(self):
        numb_ten = take_skip(20, 5)
        self.assertEqual([0, 20, 40, 60, 80], list(numb_ten))
