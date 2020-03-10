from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, qty: int):
        self.__quantity = qty


class Vegetable(Food):
    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Meat(Food):
    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Fruit(Food):
    def __init__(self, quantity: int):
        Food.__init__(self, quantity)


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    def food_eaten(self):
        return self.__food_eaten

    @food_eaten.setter
    def food_eaten(self, value):
        self.__food_eaten = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def feed(self, kind: object):
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, wing_size: float, weight: float):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    @abstractmethod
    def make_sound(self):
        pass


class Owl(Bird):
    __foods_cant_eat = ["Vegetable", "Fruit", "Seeds"]
    __weight_increase = .25

    def __init__(self, name: str, wing_size: float, weight: float):
        Bird.__init__(self, name, wing_size, weight)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Hen(Bird):
    __weight_increase = .35

    def __init__(self, name: str, wing_size: float, weight: float):
        Bird.__init__(self, name, wing_size, weight)

    def make_sound(self):
        return "Cluck"

    def feed(self, kind: object):
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


from unittest import TestCase


class OwlTests(TestCase):

    def test_owl(self):
        owl: Owl = Owl("Pip", 10, 10)
        self.assertEqual("Owl [Pip, 10, 10, 0]", str(owl))
        self.assertEqual("Hoot Hoot", owl.make_sound())
        meat: Meat = Meat(4)
        owl.feed(meat)
        veg: Vegetable = Vegetable(1)
        self.assertEqual("Owl does not eat Vegetable!", owl.feed(veg))
        self.assertEqual("Owl [Pip, 10, 11.0, 4]", str(owl))


class HenTests(TestCase):

    def test_hen(self):
        hen: Hen = Hen("Harry", 10, 10)
        veg: Vegetable = Vegetable(3)
        fruit: Fruit = Fruit(5)
        meat = Meat(1)
        self.assertEqual("Hen [Harry, 10, 10, 0]", str(hen))
        self.assertEqual("Cluck", hen.make_sound())
        hen.feed(veg)
        hen.feed(fruit)
        hen.feed(meat)
        self.assertEqual("Hen [Harry, 10, 13.15, 9]", str(hen))

if __name__ == 'main':
    TestCase.main()
