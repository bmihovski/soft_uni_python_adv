import unittest
from wild_farm_2 import Owl, Meat, Vegetable, Hen, Fruit, Dog, Seed

class OwlTests(unittest.TestCase):

    def test_owl(self):
        owl: Owl = Owl("Pip", 10, 10)
        self.assertEqual("Owl [Pip, 10, 10, 0]", str(owl))
        self.assertEqual("Hoot Hoot", owl.make_sound())
        meat: Meat = Meat(4)
        owl.feed(meat)
        veg: Vegetable = Vegetable(1)
        self.assertEqual("Owl does not eat Vegetable!", owl.feed(veg))
        self.assertEqual("Owl [Pip, 10, 11.0, 4]", str(owl))


class HenTests(unittest.TestCase):

    def test_hen(self):
        hen: Hen = Hen("Harry", 10, 10)
        veg: Vegetable = Vegetable(3)
        fruit: Fruit = Fruit(5)
        meat: Meat = Meat(1)
        self.assertEqual("Hen [Harry, 10, 10, 0]", str(hen))
        self.assertEqual("Cluck", hen.make_sound())
        hen.feed(veg)
        hen.feed(fruit)
        hen.feed(meat)
        self.assertEqual("Hen [Harry, 10, 13.15, 9]", str(hen))


class DogTests(unittest.TestCase):

    def test_dog(self):
        sharo: Dog = Dog("Sharo", 10, "sofia")
        self.assertEqual("Woof!", sharo.make_sound())
        self.assertEqual("Dog [Sharo, 10, sofia, 0]", str(sharo))
        salam: Meat = Meat(5)
        sharo.feed(salam)
        cashew: Seed = Seed(3)
        self.assertEqual("Dog does not eat Seed!", sharo.feed(cashew))
        bones: Meat = Meat(4)
        sharo.feed(bones)
        self.assertEqual("Dog [Sharo, 13.6, sofia, 9]", str(sharo))

if __name__ == 'main':
    unittest.main()
