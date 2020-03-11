def squares(num: int):
    start = 1
    while start <= num:
        yield pow(start, 2)
        start += 1


from unittest import TestCase


class SquaresTests(TestCase):

    def test_zero(self):
        squares_res = squares(5)
        self.assertEqual([1, 4, 9, 16, 25], list(squares_res))
