class Vet:
    space = 5
    clinic_animals = list()

    def __init__(self, doctor_name):
        self.doctor_name = doctor_name
        self.doctor_animals = list()

    def register_animal(self, animal_name: str):
        if len(self.clinic_animals) < self.space:
            self.doctor_animals.append(animal_name)
            self.clinic_animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return f"Not enough space"

    def unregister_animal(self, animal_name: str):
        if animal_name in self.clinic_animals:
            self.clinic_animals.remove(animal_name)
            self.doctor_animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.doctor_name} has {len(self.doctor_animals)} animals. {self.space - len(self.clinic_animals)}" \
               f" space left in the clinic"


peter: Vet = Vet("Peter")
george: Vet = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.register_animal("Pencho"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
