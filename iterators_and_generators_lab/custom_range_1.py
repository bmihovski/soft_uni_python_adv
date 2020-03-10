class custom_range:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


from unittest import TestCase

class OneToTenTests(TestCase):

    def test_zero(self):
        one_to_ten = custom_range(1, 10)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [num for num in one_to_ten])

