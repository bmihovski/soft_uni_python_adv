class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


from unittest import TestCase


class ChildTests(TestCase):
    def test_zero(self):
        child: Child = Child("icho", 10)
        self.assertEqual("icho", child.name)
        self.assertEqual(10, child.age)
