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

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
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


class Truck(Vehicle):
    SUMMER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        __summer_consumption = self.fuel_consumption + Truck.SUMMER_CONSUMPTION
        __total_consumption = (distance * __summer_consumption)
        if self.fuel_quantity - __total_consumption < 0:
            return
        self.fuel_quantity -= __total_consumption

    def refuel(self, amount: int):
        amount -= amount * 0.05
        self.fuel_quantity += amount

import unittest

class CarTests(unittest.TestCase):
    
    def test_car(self):
        car: Car = Car(20, 5)
        car.drive(3)
        self.assertEqual(2.299999999999997, car.fuel_quantity)
        car.refuel(10)
        self.assertEqual(12.299999999999997, car.fuel_quantity)


class TruckTests(unittest.TestCase):

    def test_truck(self):
        truck: Truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(17.0, truck.fuel_quantity)
        truck.refuel(50)
        self.assertEqual(64.5, truck.fuel_quantity)

if __name__ == 'main':
    unittest.main()
