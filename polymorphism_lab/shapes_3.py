from abc import ABC, abstractmethod
from math import pi


class Shapes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shapes):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shapes):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return 2 * (self.__height + self.__width)

    def calculate_perimeter(self):
        return self.__height * self.__width


from unittest import TestCase


class CircleTests(TestCase):

    def test_circle_area_perimeter(self):
        circle: Circle = Circle(5)
        self.assertEqual(78.53981633974483, circle.calculate_area())
        self.assertEqual(31.41592653589793, circle.calculate_perimeter())


class RectangleTest(TestCase):

    def test_rectangle_area_perimeter(self):
        rect: Rectangle = Rectangle(10, 20)
        self.assertEqual(60, rect.calculate_area())
        self.assertEqual(200, rect.calculate_perimeter())

if __name__ == 'main':
    TestCase.main()
