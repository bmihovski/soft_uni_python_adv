import unittest

from unit_testing_exercise.project.list import IntegerList

class IntegerListTests(unittest.TestCase):
    _INITIAL_VALUE = 3
    _ADDED_VALUE = 5

    def setUp(self):
        self.integers_list: IntegerList = IntegerList(self._INITIAL_VALUE)

    def tearDown(self):
        del self.integers_list

    def test_single_value(self):
        self.assertEqual(self.integers_list.get(0), self._INITIAL_VALUE, msg="Initial value stored.")

    def test_initial_no_value(self):
        empty_list: IntegerList = IntegerList()
        self.assertEqual(empty_list.get_data(), [], msg="When no value provided empty list")

    def test_initial_value_str(self):
        list_str: IntegerList = IntegerList('d')
        self.assertEqual(list_str.get_data(), [], msg="When initial value str value not added")

    def test_initial_value_int_str(self):
        mixed_initial: IntegerList = IntegerList(self._INITIAL_VALUE, "dee", "3", self._ADDED_VALUE)
        self.assertEqual( mixed_initial.get_data(), [self._INITIAL_VALUE, self._ADDED_VALUE],
                         msg="When initial data mixed only integers added")

    def test_add_element(self):
        self.assertEqual(self.integers_list.add(self._ADDED_VALUE), [self._INITIAL_VALUE, self._ADDED_VALUE],
                         msg="Int values can't be added with add function")

    def test_add_str_element_exception(self):
        with self.assertRaises(ValueError) as si:
            self.integers_list.add("d")
        when_value_str_exception = si.exception
        self.assertEqual(when_value_str_exception.__str__(), "Element is not Integer", msg="Strings can't be added")

    def test_remove_element(self):
        self.assertEqual(self.integers_list.remove_index(0), self._INITIAL_VALUE, msg="Element not removed")

    def test_remove_element_out_of_index(self):
        with self.assertRaises(IndexError) as wi:
            self.integers_list.remove_index(129)
        elem_out_of_index_exception = wi.exception
        self.assertEqual(elem_out_of_index_exception.__str__(), "Index is out of range",
                         msg="Elem with wrong index can't be removed")

    def test_get_element(self):
        self.assertEqual(self._INITIAL_VALUE, self.integers_list.get(0), msg="Correct element should be returned")

    def test_get_element_out_of_index(self):
        with self.assertRaises(IndexError) as ne:
            self.integers_list.get(199)
        non_existent_index_exception = ne.exception
        self.assertEqual(non_existent_index_exception.__str__(), "Index is out of range",
                         msg="Element with not existent index can not be called")

if __name__ == '__main__':
    unittest.main()
