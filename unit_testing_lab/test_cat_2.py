class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    _IS_FED = True
    _IS_SLEEPY = False

    def setUp(self):
        self.cat_under_test: Cat = Cat("olld")

    def tearDown(self):
        del self.cat_under_test

    def test_cat_size_increased(self):
        self.cat_under_test.eat()
        self.assertEqual(1, self.cat_under_test.size, msg="Cat should gain weight when eat.")

    def test_cat_is_fed(self):
        self.cat_under_test.eat()
        self.assertEqual(self._IS_FED, self.cat_under_test.fed, msg="When cat eat should be fed.")

    def test_cat_is_fed_error(self):
        self.cat_under_test.eat()
        with self.assertRaises(Exception) as cf:
            self.cat_under_test.eat()
        cat_is_already_fed_exception = cf.exception
        self.assertEqual("Already fed.", cat_is_already_fed_exception.__str__(),
                         msg="Proper message is displayed when cat is already fed.")

    def test_cat_not_fed_cant_sleep(self):
        with self.assertRaises(Exception) as cs:
            self.cat_under_test.sleep()
        cat_not_fed_cant_sleep_exception = cs.exception
        self.assertEqual("Cannot sleep while hungry", cat_not_fed_cant_sleep_exception.__str__(),
                         msg="Proper message is displayed when cat is hungry and forced to sleep.")

    def test_cat_not_sleepy_after_sleep(self):
        self.cat_under_test.eat()
        self.cat_under_test.sleep()
        self.assertEqual(self._IS_SLEEPY, self.cat_under_test.sleepy, msg="When cat sleep is not sleepy")


if __name__ == '__main__':
    unittest.main()
