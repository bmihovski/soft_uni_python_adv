class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    _WORKER_NAME = "test"
    _WORKER_SALARY = 34
    _WORKER_ENERGY = 23

    def setUp(self):
        self.worker_under_test: Worker = Worker(self._WORKER_NAME, self._WORKER_SALARY, self._WORKER_ENERGY)

    def tearDown(self):
        del self.worker_under_test

    def test_correct_instance(self):
        self.assertEqual(self._WORKER_NAME, self.worker_under_test.name, msg="Worker name should be set up.")
        self.assertEqual(self._WORKER_SALARY, self.worker_under_test.salary, msg="Worker salary should be set up.")
        self.assertEqual(self._WORKER_ENERGY, self.worker_under_test.energy, msg="Worker energy should be set up.")

    def test_energy_incr(self):
        self.worker_under_test.rest()
        self.assertEqual(self._WORKER_ENERGY + 1, self.worker_under_test.energy,
                         msg="When rest worker energy increased.")

    def test_energy_neg(self):
        self.worker_under_test.energy = 0
        with self.assertRaises(Exception) as em:
            self.worker_under_test.work()
        worker_exception = em.exception
        self.assertEqual("Not enough energy.", worker_exception.__str__(),
                         msg="Message displayed when worker is forced to work no energy")

    def test_salary_increased(self):
        self.worker_under_test.work()
        self.assertEqual(self._WORKER_SALARY, self.worker_under_test.salary,
                         msg="Worker salary increased after work.")
        self.assertEqual(self._WORKER_ENERGY - 1, self.worker_under_test.energy,
                         msg="Worker salary decreased after work.")

    def test_worker_info(self):
        self.assertEqual(f"{self._WORKER_NAME} has saved 0 money.", self.worker_under_test.get_info(),
                         msg="Correct info displayed for worker which didn't work")
        self.worker_under_test.work()
        self.assertEqual(f"{self._WORKER_NAME} has saved {self._WORKER_SALARY} money.", self.worker_under_test.get_info(),
                         msg="Correct info displayed when worker worked")


if __name__ == '__main__':
    unittest.main()
