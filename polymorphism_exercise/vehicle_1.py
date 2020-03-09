from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, amount: int):
        pass


class Car(Vehicle):
    SUMMER_CONSUMPTION = .9

    def __init__(self, fuel_quantity: int, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        __summer_consumption = self.fuel_consumption + Car.SUMMER_CONSUMPTION
        __total_consumption = (distance * __summer_consumption)
        if self.fuel_quantity - __total_consumption < 0:
            return
        self.fuel_quantity -= __total_consumption

    def refuel(self, amount: int):
        self.fuel_quantity += amount

from unittest import TestCase


class CarTests(TestCase):

    def test_car(self):
        car: Car = Car(20, 5)
        car.drive(3)
        self.assertEqual(2.299999999999997, car.fuel_quantity)
        car.refuel(10)
        self.assertEqual(12.299999999999997, car.fuel_quantity)

if __name__ == 'main':
    TestCase.main()