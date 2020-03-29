import unittest
from unit_testing_exercise.project.car_manager import Car

class CarTests(unittest.TestCase):
    _INITIAL_MAKE = "honda"
    _INITIAL_MODEL = "civic"
    _INITIAL_FUEL_CONSUMPTION = 2
    _INITIAL_FUEL_CAPACITY = 20
    _REFUEL_AMOUNT = 5

    def setUp(self):
        self.test_car = Car(self._INITIAL_MAKE, self._INITIAL_MODEL,
                            self._INITIAL_FUEL_CONSUMPTION, self._INITIAL_FUEL_CAPACITY)

    def tearDown(self):
        del self.test_car

    def test_when_make_then_correct_value(self):
        self.assertEqual(self.test_car.make, self._INITIAL_MAKE,
                         msg="Car should have make")

    def test_when_make_empty_then_exception(self):
        with self.assertRaises(Exception) as nm:
            self.test_car.make = ''
        make_empty_exception = nm.exception
        self.assertEqual(make_empty_exception.__str__(), "Make cannot be null or empty!",
                         msg="Make value can't be empty")

    def test_when_model_then_correct_value(self):
        self.assertEqual(self.test_car.model, self._INITIAL_MODEL,
                         msg="Car should have model")

    def test_when_model_empty_then_exception(self):
        with self.assertRaises(Exception) as nm:
            self.test_car.model = ''
        model_empty_exception = nm.exception
        self.assertEqual(model_empty_exception.__str__(), "Model cannot be null or empty!",
                         msg="Model value can't be empty")

    def test_when_fuel_consumption_then_correct_value(self):
        self.assertEqual(self.test_car.fuel_consumption, self._INITIAL_FUEL_CONSUMPTION,
                         msg="Fuel consumption should be correct")

    def test_when_fuel_consumption_zero_then_exception(self):
        with self.assertRaises(Exception) as zv:
            self.test_car.fuel_consumption = 0
        fuel_consumption_exception = zv.exception
        self.assertEqual(fuel_consumption_exception.__str__(), "Fuel consumption cannot be zero or negative!",
                         msg="Fuel consumption can't be zero")

    def test_when_fuel_consumption_str_then_exception(self):
        with self.assertRaises(TypeError) as sv:
            self.test_car.fuel_consumption = "dfd"
        fuel_consumption_exception = sv.exception
        self.assertEqual(fuel_consumption_exception.__str__(), "'<=' not supported between instances of 'str' and 'int'",
                         msg="Fuel consumption can't be string")

    def test_when_fuel_capacity_then_correct_value(self):
        self.assertEqual(self.test_car.fuel_capacity, self._INITIAL_FUEL_CAPACITY,
                         msg="Fuel capacity value should be correct")

    def test_when_fuel_capacity_str_then_exception(self):
        with self.assertRaises(TypeError) as sv:
            self.test_car.fuel_capacity = "fs"
        fuel_capacity_exception = sv.exception
        self.assertEqual(fuel_capacity_exception.__str__(), "'<=' not supported between instances of 'str' and 'int'",
                         msg="Fuel capacity can't be string")

    def test_when_fuel_capacity_zero_then_exception(self):
        with self.assertRaises(Exception) as zv:
            self.test_car.fuel_capacity = 0
        fuel_capacity_exception = zv.exception
        self.assertEqual(fuel_capacity_exception.__str__(), "Fuel capacity cannot be zero or negative!",
                         msg="Fuel capacity can't be zero")

    def test_when_fuel_amount_negative_then_exception(self):
        with self.assertRaises(Exception) as nv:
            self.test_car.fuel_amount = -1
        fuel_amount_exception = nv.exception
        self.assertEqual(fuel_amount_exception.__str__(), "Fuel amount cannot be negative!",
                         msg="Fuel amount can't be negative")

    def test_when_fuel_amount_then_correct_value(self):
        self.test_car.fuel_amount = 4
        self.assertEqual(4, self.test_car.fuel_amount,
                         msg="Fuel amount should be correct")

    def test_when_refuel_then_fuel_amount_increased(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        self.assertEqual(self.test_car.fuel_amount, self._REFUEL_AMOUNT,
                         msg="Fuel amount is as the refueled")

    def test_when_refuel_negative_then_exception(self):
        with self.assertRaises(Exception) as mf:
            self.test_car.refuel(-300)
        refuel_over_exception = mf.exception
        self.assertEqual(refuel_over_exception.__str__(), "Fuel amount cannot be zero or negative!",
                         msg="You can't refuel with negative value")

    def test_when_refuel_over_fuel_capacity_then_fuel_amount_to_fuel_capacity(self):
        self.test_car.refuel(1000)
        self.assertEqual(self.test_car.fuel_amount, self._INITIAL_FUEL_CAPACITY,
                         msg="You can't have more fuel than fuel capacity")

    def test_when_drive_then_success(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        __fuel_amount_before_drive = self.test_car.fuel_amount
        self.test_car.drive(50)
        self.assertEqual(self.test_car.fuel_amount, __fuel_amount_before_drive - 1,
                         msg="Fuel amount is correct")

    def test_when_drive_and_not_enough_fuel_then_exception(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        with self.assertRaises(Exception) as nef:
            self.test_car.drive(1000)
        not_enough_fuel_exception = nef.exception
        self.assertEqual(not_enough_fuel_exception.__str__(), "You don't have enough fuel to drive!",
                         msg="You should have enough fuel to drive")

if __name__ == '__main__':
    unittest.main()
