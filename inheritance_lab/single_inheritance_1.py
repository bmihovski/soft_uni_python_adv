class Animal:
    def __init__(self):
        pass

    def eat(self):
        return "eating..."


class Dog(Animal):
    def __init__(self):
        pass

    def bark(self):
        return "barking..."


dog: Dog = Dog()
print(dog.eat())
print(dog.bark())
