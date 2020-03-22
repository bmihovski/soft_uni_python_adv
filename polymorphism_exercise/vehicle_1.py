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
