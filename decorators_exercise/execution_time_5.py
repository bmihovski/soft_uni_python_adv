from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        stop_time = time()
        time_difference = stop_time - start_time
        return time_difference
    return wrapper


from unittest import TestCase


class ExecutionTime(TestCase):
    def test_loop(self):
        @exec_time
        def loop(start, end):
            total = 0
            for x in range(start, end):
                total += x
            return total
        self.assertEqual(1, round(loop(1, 10000000)))

    def test_concatenate(self):
        @exec_time
        def concatenate(strings):
            result = ""
            for string in strings:
                result += string
            return result

        self.assertEqual(0, round(concatenate(["a" for i in range(1000000)])))
