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


class Seeds(Food):
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

    @abstractmethod
    def make_sound(self):
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, wing_size: float, weight: float):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    @property
    def wing_size(self):
        return self.__wing_size

    @wing_size.setter
    def wing_size(self, size: float):
        self.__wing_size = size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


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


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        Animal.__init__(self, name, weight)
        self.living_region = living_region

    @property
    def living_region(self):
        return self.__living_region

    @living_region.setter
    def living_region(self, region: str):
        self.__living_region = region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    __weight_increase = .4
    __foods_cant_eat = ["Vegetable", "Fruit", "Seeds"]

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Tiger(Mammal):
    __weight_increase = 1.0
    __foods_cant_eat = ["Vegetable", "Fruit", "Seeds"]

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Cat(Mammal):
    __weight_increase = .3
    __foods_cant_eat = ["Fruit", "Seeds"]

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Mouse(Mammal):
    __weight_increase = .1
    __foods_cant_eat = ["Meat", "Seeds"]

    def __init__(self, name: str, weight: float, living_region: str):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
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


class DogTests(TestCase):

    def test_dog(self):
        sharo: Dog = Dog("Sharo", 10, "sofia")
        self.assertEqual("Woof!", sharo.make_sound())
        self.assertEqual("Dog [Sharo, 10, sofia, 0]", str(sharo))
        salam: Meat = Meat(5)
        sharo.feed(salam)
        cashew: Seeds = Seeds(3)
        self.assertEqual("Dog does not eat Seeds!", sharo.feed(cashew))
        bones: Meat = Meat(4)
        sharo.feed(bones)
        self.assertEqual("Dog [Sharo, 13.6, sofia, 9]", str(sharo))

if __name__ == 'main':
    TestCase.main()
