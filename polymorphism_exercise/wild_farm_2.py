from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
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
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

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
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
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
    __foods_cant_eat = ["Vegetable", "Fruit", "Seed"]
    __weight_increase = .25

    def __init__(self, name: str, wing_size: float, weight: float):
        super().__init__(name, wing_size, weight)

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
        super().__init__(name, wing_size, weight)

    def make_sound(self):
        return "Cluck"

    def feed(self, kind: object):
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
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
    __foods_cant_eat = ["Vegetable", "Fruit", "Seed"]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Tiger(Mammal):
    __weight_increase = 1.0
    __foods_cant_eat = ["Vegetable", "Fruit", "Seed"]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Cat(Mammal):
    __weight_increase = .3
    __foods_cant_eat = ["Fruit", "Seed"]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase


class Mouse(Mammal):
    __weight_increase = .1
    __foods_cant_eat = ["Meat", "Seed"]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, kind: object):
        if kind.__class__.__name__ in self.__foods_cant_eat:
            return f"{self.__class__.__name__} does not eat {kind.__class__.__name__}!"
        self.food_eaten += kind.quantity
        self.weight += kind.quantity * self.__weight_increase
