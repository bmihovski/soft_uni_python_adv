def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


from unittest import TestCase


class FibGenTests(TestCase):
    def test_zero(self):
        results = list()
        generator = fibonacci()
        for i in range(5):
            results.append(next(generator))
        self.assertEqual([0, 1, 1, 2, 3], results)
