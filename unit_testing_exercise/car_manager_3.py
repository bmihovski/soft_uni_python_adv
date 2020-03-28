class Car:
    def __init__(self, make="", model="", fuel_consumption=0, fuel_capacity=0):
        self.__make = make
        self.__model = model
        self.__fuel_consumption = fuel_consumption
        self.__fuel_capacity = fuel_capacity
        self.__fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Provide string value for Car make")
        if type(new_value) != str:
            raise ValueError("Provide string for Car make")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Provide string value for Car model")
        if type(new_value) != str:
            raise ValueError("Provide string for Car model")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if type(new_value) != int:
            raise TypeError("Fuel consumption can be integer only")
        if new_value <= 0:
            raise Exception("Only positive fuel consumption allowed")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if type(new_value) != int:
            raise TypeError("Fuel capacity can be integer only")
        if new_value <= 0:
            raise Exception("Only positive fuel consumption allowed")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise ValueError("Fuel can't be zero or negative")
        self.fuel_amount += fuel
        if self.fuel_amount + fuel > self.fuel_capacity:
            self.fuel_amount = self.fuel_capacity

    def drive(self, distance):
        __burned_fuel = (self.fuel_consumption / 100) * distance
        if self.fuel_amount - __burned_fuel < 0:
            raise Exception("Not enough fuel to drive!")
        self.fuel_amount -= __burned_fuel


import unittest


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
        self.assertEqual(self._INITIAL_MAKE, self.test_car.make,
                         msg="Car should have make")

    def test_when_make_int_then_exception(self):
        with self.assertRaises(ValueError) as im:
            self.test_car.make = 3
        make_only_str_exception = im.exception
        self.assertEqual("Provide string for Car make", make_only_str_exception.__str__(),
                         msg="Make can be string only")

    def test_when_make_empty_then_exception(self):
        with self.assertRaises(Exception) as nm:
            self.test_car.make = ''
        make_empty_exception = nm.exception
        self.assertEqual("Provide string value for Car make", make_empty_exception.__str__(),
                         msg="Make value can't be empty")

    def test_when_model_then_correct_value(self):
        self.assertEqual(self._INITIAL_MODEL, self.test_car.model,
                         msg="Car should have model")

    def test_when_model_empty_then_exception(self):
        with self.assertRaises(Exception) as nm:
            self.test_car.model = ''
        model_empty_exception = nm.exception
        self.assertEqual("Provide string value for Car model", model_empty_exception.__str__(),
                         msg="Model value can't be empty")

    def test_when_model_int_then_correct_value(self):
        with self.assertRaises(ValueError) as im:
            self.test_car.model = 3
        model_only_str_exception = im.exception
        self.assertEqual("Provide string for Car model", model_only_str_exception.__str__(),
                         msg="Model can be string only")

    def test_when_fuel_consumption_then_correct_value(self):
        self.assertEqual(self._INITIAL_FUEL_CONSUMPTION, self.test_car.fuel_consumption,
                         msg="Fuel consumption should be correct")

    def test_when_fuel_consumption_zero_then_exception(self):
        with self.assertRaises(Exception) as zv:
            self.test_car.fuel_consumption = 0
        fuel_consumption_exception = zv.exception
        self.assertEqual("Only positive fuel consumption allowed", fuel_consumption_exception.__str__(),
                         msg="Fuel consumption can't be zero")

    def test_when_fuel_consumption_str_then_exception(self):
        with self.assertRaises(TypeError) as sv:
            self.test_car.fuel_consumption = "dfd"
        fuel_consumption_exception = sv.exception
        self.assertEqual("Fuel consumption can be integer only", fuel_consumption_exception.__str__(),
                         msg="Fuel consumption can't be string")

    def test_when_fuel_capacity_then_correct_value(self):
        self.assertEqual(self._INITIAL_FUEL_CAPACITY, self.test_car.fuel_capacity,
                         msg="Fuel capacity value should be correct")

    def test_when_fuel_capacity_str_then_exception(self):
        with self.assertRaises(TypeError) as sv:
            self.test_car.fuel_capacity = "fs"
        fuel_capacity_exception = sv.exception
        self.assertEqual("Fuel capacity can be integer only", fuel_capacity_exception.__str__(),
                         msg="Fuel capacity can't be string")

    def test_when_fuel_capacity_zero_then_exception(self):
        with self.assertRaises(Exception) as zv:
            self.test_car.fuel_capacity = 0
        fuel_capacity_exception = zv.exception
        self.assertEqual("Only positive fuel consumption allowed", fuel_capacity_exception.__str__(),
                         msg="Fuel capacity can't be zero")

    def test_when_fuel_amount_negative_then_exception(self):
        with self.assertRaises(Exception) as nv:
            self.test_car.fuel_amount = -1
        fuel_amount_exception = nv.exception
        self.assertEqual("Fuel amount cannot be negative!", fuel_amount_exception.__str__(),
                         msg="Fuel amount can't be negative")

    def test_when_fuel_amount_then_correct_value(self):
        self.test_car.fuel_amount = 4
        self.assertEqual(4, self.test_car.fuel_amount,
                         msg="Fuel amount should be correct")

    def test_when_refuel_then_fuel_amount_increased(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        self.assertEqual(self._REFUEL_AMOUNT, self.test_car.fuel_amount,
                         msg="Fuel amount is as the refueled")

    def test_when_refuel_negative_then_exeption(self):
        with self.assertRaises(ValueError) as mf:
            self.test_car.refuel(-300)
        refuel_over_exception = mf.exception
        self.assertEqual("Fuel can't be zero or negative", refuel_over_exception.__str__(),
                         msg="You can't refuel with negative value")

    def test_when_refuel_over_fuel_capacity_then_fuel_amount_to_fuel_capacity(self):
        self.test_car.refuel(1000)
        self.assertEqual(self._INITIAL_FUEL_CAPACITY, self.test_car.fuel_amount,
                         msg="You can't have more fuel than fuel capacity")

    def test_when_drive_then_success(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        __fuel_amount_before_drive = self.test_car.fuel_amount
        self.test_car.drive(50)
        self.assertEqual(__fuel_amount_before_drive - 1, self.test_car.fuel_amount,
                         msg="Fuel amount is correct")

    def test_when_drive_and_not_enough_fuel_then_exception(self):
        self.test_car.refuel(self._REFUEL_AMOUNT)
        with self.assertRaises(Exception) as nef:
            self.test_car.drive(1000)
        not_enough_fuel_exception = nef.exception
        self.assertEqual("Not enough fuel to drive!", not_enough_fuel_exception.__str__(),
                         msg="You should have enough fuel to drive")

if __name__ == '__main__':
    unittest.main()
