import unittest
from vehicle_1 import Car, Truck

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
