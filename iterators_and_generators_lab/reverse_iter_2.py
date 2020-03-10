class reverse_iter:
    def __init__(self, nums: list):
        self.nums = nums
        self.__start = len(self.nums)

    def __iter__(self):
        return self

    def __next__(self):
        if not len(self.nums) or self.__start == 0:
            raise StopIteration
        else:
            self.__start -= 1
            return self.nums[self.__start]


from unittest import TestCase


class TenToOneTests(TestCase):

    def test_zero(self):
        ten_to_one = reverse_iter([1, 2, 3, 4])
        self.assertEqual([4, 3, 2, 1], [num for num in ten_to_one])
