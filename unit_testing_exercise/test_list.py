import unittest

from project.list import IntegerList

class IntegerListTests(unittest.TestCase):
    _INITIAL_VALUE = 3
    _ADDED_VALUE = 5

    def setUp(self):
        self.integers_list: IntegerList = IntegerList(self._INITIAL_VALUE)

    def tearDown(self):
        del self.integers_list

    def test_single_value(self):
        self.assertEqual(self._INITIAL_VALUE, self.integers_list.get(0), msg="Initial value stored.")

    def test_initial_no_value(self):
        empty_list: IntegerList = IntegerList()
        self.assertEqual([], empty_list.get_data(), msg="When no value provided empty list")

    def test_initial_value_str(self):
        list_str: IntegerList = IntegerList('d')
        self.assertEqual([], list_str.get_data(), msg="When initial value str value not added")

    def test_initial_value_int_str(self):
        mixed_initial: IntegerList = IntegerList(self._INITIAL_VALUE, "dee", "3", self._ADDED_VALUE)
        self.assertEqual([self._INITIAL_VALUE, self._ADDED_VALUE], mixed_initial.get_data(),
                         msg="When initial data mixed only integers added")

    def test_add_element(self):
        self.assertEqual([self._INITIAL_VALUE, self._ADDED_VALUE], self.integers_list.add(self._ADDED_VALUE),
                         msg="Int values can't be added with add function")

    def test_add_str_element_exception(self):
        with self.assertRaises(ValueError) as si:
            self.integers_list.add("d")
        when_value_str_exeption = si.exception
        self.assertEqual("Element is not Integer", when_value_str_exeption.__str__(), msg="Strings can't be added")

    def test_remove_element(self):
        self.assertEqual(self._INITIAL_VALUE, self.integers_list.remove_index(0), msg="Element not removed")

    def test_remove_element_out_of_index(self):
        with self.assertRaises(IndexError) as wi:
            self.integers_list.remove_index(129)
        elem_out_of_index_exception = wi.exception
        self.assertEqual("Index is out of range", elem_out_of_index_exception.__str__(),
                         msg="Elem with wrong index can't be removed")

    def test_get_element(self):
        self.assertEqual(self._INITIAL_VALUE, self.integers_list.get(0), msg="Correct element should be returned")

    def test_get_element_out_of_index(self):
        with self.assertRaises(IndexError) as ne:
            self.integers_list.get(199)
        non_existent_index_exception = ne.exception
        self.assertEqual("Index is out of range", non_existent_index_exception.__str__(),
                         msg="Element with not existent index can not be called")

if __name__ == '__main__':
    unittest.main()
