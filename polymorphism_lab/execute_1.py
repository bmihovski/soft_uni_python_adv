def single_arg(text):
    return text


def multi_args(name, family):
    return f'{name} {family}'


def execute(func, *args):
    return func(*args)


import unittest


class ExecuteTests(unittest.TestCase):

    def test_single_arg(self):
        self.assertEqual("eee", execute(single_arg, "eee"))

    def test_multi_args(self):
        self.assertEqual("Ceco Pepe", execute(multi_args, "Ceco", "Pepe"))


if __name__ == 'main':
    unittest.main()
