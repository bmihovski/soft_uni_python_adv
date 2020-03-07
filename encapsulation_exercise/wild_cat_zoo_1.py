from functools import reduce


class Lion:
    __lions_need = 50

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_need(self):
        return self.__lions_need

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:
    __tigers_need = 45

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_need(self):
        return self.__tigers_need

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:
    __cheetahs_need = 60

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_need(self):
        return self.__cheetahs_need

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: object, price: int):
        if self.__animal_capacity > 0 and self.__budget == 0:
            return "Not enough budget"
        if self.__animal_capacity == 0:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        self.__animal_capacity -= 1
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: object):
        if self.__workers_capacity == 0:
            return "Not enough space for worker"
        self.workers.append(worker)
        self.__workers_capacity -= 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        __worker_to_fire = list(filter(lambda worker_to_check: worker_to_check.name != worker_name, self.workers))
        if len(__worker_to_fire) == len(self.workers):
            return f"There is no {worker_name} in the zoo"
        self.workers = __worker_to_fire
        self.__workers_capacity += 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        __salaries_to_pay = reduce(lambda acc, hire: acc + hire.salary, self.workers, 0)
        if self.__budget - __salaries_to_pay < 0:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= __salaries_to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        __total_tend_cost = reduce(lambda acc, animal_to_tend: acc + animal_to_tend.get_need(), self.animals, 0)
        if self.__budget - __total_tend_cost < 0:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= __total_tend_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        __lions = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Lion", self.animals))
        __tigers = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Tiger", self.animals))
        __cheetahs = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Cheetah", self.animals))
        __total_animals_count = f"You have {len(self.animals)} animals \n"
        __total_lions = f"----- {len(__lions)} Lions:\n"
        __each_lion = "\n".join([lion.__repr__() for lion in __lions])
        __total_tigers = f"\n----- {len(__tigers)} Tigers:\n"
        __each_tiger = "\n".join([tiger.__repr__() for tiger in __tigers])
        __total_cheetahs = f"\n----- {len(__cheetahs)} Cheetahs:\n"
        __each_cheetahs = "\n".join([cheetah.__repr__() for cheetah in __cheetahs])

        return __total_animals_count + __total_lions + __each_lion + __total_tigers + \
               __each_tiger + __total_cheetahs + __each_cheetahs

    def workers_status(self):
        __keepers = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Keeper", self.workers))
        __caretakers = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Caretaker",
                                   self.workers))
        __vets = list(filter(lambda animal_to_check: animal_to_check.__class__.__name__ == "Vet", self.workers))
        __total_workers_count = f"\nYou have {len(self.workers)} workers\n"
        __total_keepers = f"----- {len(__keepers)} Keepers:\n"
        __each_keeper = "\n".join([keeper.__repr__() for keeper in __keepers])
        __total_caretakers = f"\n----- {len(__caretakers)} Caretakers:\n"
        __each_caretaker = "\n".join([caretaker.__repr__() for caretaker in __caretakers])
        __total_vets = f"\n----- {len(__vets)} Vets:\n"
        __each_vet = "\n".join([vet.__repr__() for vet in __vets])

        return __total_workers_count + __total_keepers + __each_keeper + __total_caretakers + __each_caretaker +\
               __total_vets + __each_vet


zoo: Zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
