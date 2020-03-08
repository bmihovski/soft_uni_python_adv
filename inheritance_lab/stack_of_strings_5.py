class Stack():
    def __init__(self):
        self.__data = list()

    def push(self, item):
        self.__data.insert(0, item)

    def pop(self):
        return self.__data.pop(0)

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return False if len(self.__data) > 0 else True

    def __str__(self):
        return str(self.__data)


import unittest

class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(str(stack), "[2, 1]")
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        stack.push(5)
        self.assertEqual(str(stack), "[5, 1]")
        self.assertEqual(stack.is_empty(), False)

if __name__ == '__main__':
    unittest.main()
