import random


class RandomList(list):
    def __init__(self):
        list.__init__(self)

    def get_random_element(self):
        random_el = random.choice(self)
        self.remove(random_el)
        return random_el


# test first zero
import unittest
from unittest import mock


class RandomListTests(unittest.TestCase):
    def test_zero_first(self):
        with mock.patch('random.choice', lambda x: 4):
            li = RandomList()
            li.append(4)
            li.append(3)
            li.append(5)
            li.pop()
            li.reverse()
            self.assertEqual(sum(li), 7)
            self.assertEqual(li.get_random_element(), 4)


if __name__ == '__main__':
    unittest.main()
