class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == -1:
            raise StopIteration
        else:
            self.count -= 1
            return self.count + 1


from unittest import TestCase


class CountDownIteratorTests(TestCase):
    def test_zero(self):
        iterator = countdown_iterator(10)
        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], list(iterator))
