def cache(func):
    def wrapper(num: int):
        result = func(num)
        wrapper.log[num] = result
        return result
    wrapper.log = dict()
    return wrapper


from unittest import TestCase


class CacheTests(TestCase):
    def test_zero_first(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)

        fibonacci(3)
        self.assertEqual({1: 1, 0: 0, 2: 1, 3: 2}, fibonacci.log)
        fibonacci(4)
        self.assertEqual({1: 1, 0: 0, 2: 1, 3: 2, 4: 3}, fibonacci.log)
