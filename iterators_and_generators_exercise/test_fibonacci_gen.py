import unittest
from fibonacci_generator_5 import fibonacci

class FibGenTests(unittest.TestCase):
    def test_zero(self):
        results = list()
        generator = fibonacci()
        for i in range(5):
            results.append(next(generator))
        self.assertEqual([0, 1, 1, 2, 3], results)

if __name__ == 'main':
    unittest.main()
