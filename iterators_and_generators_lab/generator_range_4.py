def genrange(start: int, stop: int):

    while start <= stop:
        yield start
        start += 1


from unittest import TestCase


class GenRangeTests(TestCase):

    def test_zero(self):
        gen_range = genrange(1, 10)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], list(gen_range))