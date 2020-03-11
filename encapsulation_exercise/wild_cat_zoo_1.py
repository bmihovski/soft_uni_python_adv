from functools import reduce


class Lion:
    __lions_need = 50

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return self.__lions_need

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:
    __tigers_need = 45

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return self.__tigers_need

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:
    __cheetahs_need = 60

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
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
        if self.__animal_capacity > 0 and self.__budget - price <= 0:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        #self.__animal_capacity -= 1
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: object):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        #self.__workers_capacity -= 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        __workers_to_stay = list(filter(lambda worker_to_check: worker_to_check.name != worker_name, self.workers))
        if len(__workers_to_stay) == len(self.workers):
            return f"There is no {worker_name} in the zoo"
        self.workers = __workers_to_stay
        #self.__workers_capacity += 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        __salaries_to_pay = reduce(lambda acc, hire: acc + hire.salary, self.workers, 0)
        if self.__budget - __salaries_to_pay <= 0:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= __salaries_to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        __total_tend_cost = reduce(lambda acc, animal_to_tend: acc + animal_to_tend.get_needs(), self.animals, 0)
        if self.__budget - __total_tend_cost <= 0:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= __total_tend_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    @staticmethod
    def __is_type(type_to_check: str):
        return lambda type_checked: type_checked.__class__.__name__ == type_to_check

    @staticmethod
    def __generate_status(types: list):
        results = list()
        total_types = f"----- {len(types)} {types[0].__class__.__name__}s:"
        results.append(total_types)
        for each_type in types:
            each_type = each_type.__repr__()
            results.append(each_type)
        return results

    # def animals_status(self):
    #     __lions = list(filter(self.__is_type("Lion"), self.animals))
    #     __tigers = list(filter(self.__is_type("Tiger"), self.animals))
    #     __cheetahs = list(filter(self.__is_type("Cheetah"), self.animals))
    #     __total_animals_count = f"You have {len(self.animals)} animals"
    #     __lion_results = Zoo.__generate_status(__lions)
    #     __tiger_results = Zoo.__generate_status(__tigers)
    #     __cheetah_results = Zoo.__generate_status(__cheetahs)
    #     return "\n".join([__total_animals_count, *__lion_results, *__tiger_results, *__cheetah_results])

    # def workers_status(self):
    #     __keepers = list(filter(self.__is_type("Keeper"), self.workers))
    #     __caretakers = list(filter(self.__is_type("Caretaker"), self.workers))
    #     __vets = list(filter(self.__is_type("Vet"), self.workers))
    #     __total_workers_count = f"You have {len(self.workers)} workers"
    #     __keeper_results = Zoo.__generate_status(__keepers)
    #     __caretaker_results = Zoo.__generate_status(__caretakers)
    #     __vet_results = Zoo.__generate_status(__vets)
    #     return "\n".join([__total_workers_count, *__keeper_results, *__caretaker_results, *__vet_results])

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        for animal_type in ("Lion", "Tiger", "Cheetah"):
            result += f"----- {len([animal for animal in self.animals if animal_type == animal.__class__.__name__])} {animal_type}s:\n"
            for single_animal in [animal for animal in self.animals if animal_type == animal.__class__.__name__]:
                result += f"{repr(single_animal)}\n"
        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"
        for worker_type in ("Keeper", "Caretaker", "Vet"):
            result += f"----- {len([worker for worker in self.workers if worker_type == worker.__class__.__name__])} {worker_type}s:\n"
            for single_worker in [worker for worker in self.workers if worker_type == worker.__class__.__name__]:
                result += f"{repr(single_worker)}\n"
        return result


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
