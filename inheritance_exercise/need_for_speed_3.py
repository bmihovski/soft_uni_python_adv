class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        __fuel_consumption = kilometers * self.fuel_consumption
        if self.fuel >= __fuel_consumption:
            self.fuel -= __fuel_consumption


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class Motorcycle(Vehicle):
    pass


class CrossMotorcycle(Motorcycle):
    pass


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


from unittest import TestCase


class VehicleTests(TestCase):
    def test_zero(self):
        vehicle_no_petrol: Vehicle = Vehicle(4, 33)
        vehicle_no_petrol.drive(10)
        self.assertEqual(4, vehicle_no_petrol.fuel)
        vehicle_full_tank: Vehicle = Vehicle(300, 443)
        vehicle_full_tank.drive(20)
        vehicle_full_tank.drive(200)
        self.assertEqual(25, vehicle_full_tank.fuel)


class CarTests(TestCase):
    def test_zero(self):
        car_has_petrol: Car = Car(40, 232)
        car_has_petrol.drive(10)
        car_has_petrol.drive(1)
        self.assertEqual(7, car_has_petrol.fuel)


class FamilyCarTests(TestCase):
    def test_zero(self):
        family_car_has_petrol: FamilyCar = FamilyCar(300, 443)
        family_car_has_petrol.drive(20)
        self.assertEqual(240, family_car_has_petrol.fuel)


class SportCarTests(TestCase):
    def test_zero(self):
        sport_car_has_petrol: SportCar = SportCar(150, 343)
        sport_car_has_petrol.drive(10)
        self.assertEqual(50, sport_car_has_petrol.fuel)


class MotorcycleTests(TestCase):
    def test_zero(self):
        motorcycle_has_petrol: Motorcycle = Motorcycle(200, 3434)
        motorcycle_has_petrol.drive(20)
        self.assertEqual(175, motorcycle_has_petrol.fuel)


class CrossMotorcycleTests(TestCase):
    def test_zero(self):
        cross_motorcycle_has_petrol: CrossMotorcycle = CrossMotorcycle(200, 2333)
        cross_motorcycle_has_petrol.drive(20)
        self.assertEqual(175, cross_motorcycle_has_petrol.fuel)


class RaceMotorcycleTests(TestCase):
    def test_zero(self):
        race_motorcycle_has_petrol: RaceMotorcycle = RaceMotorcycle(4333, 3432)
        race_motorcycle_has_petrol.drive(344)
        self.assertEqual(1581, race_motorcycle_has_petrol.fuel)

