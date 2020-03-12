class dictionary_iter:
    __counter = 0

    def __init__(self, input_dict: dict):
        self.input_dict = input_dict

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter == len(self.input_dict):
            raise StopIteration
        else:
            self.__counter += 1
            list_items = list(self.input_dict.items())
            return list_items[self.__counter - 1]


from unittest import TestCase


class DictIterTests(TestCase):

    def test_zero(self):
        result = dictionary_iter({1: "a", 2: "d"})
        self.assertEqual([(1, 'a'), (2, 'd')], list(result))
