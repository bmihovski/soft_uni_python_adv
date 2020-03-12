def logged(func):
    def wrapper(*args):
        return f'you called {func.__name__}{args}\nit returned {func(*args)}'
    return wrapper


from unittest import TestCase


class LoggedTests(TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        self.assertEqual('you called func(4, 4, 4)\nit returned 6', func(4, 4, 4))
