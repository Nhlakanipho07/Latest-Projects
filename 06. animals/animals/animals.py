class Animal:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")

        self._name = name

    def sound(self):
        return "sound..."

    def eat(self):
        return f"{self._name} eats"


class Dog(Animal):
    def __init__(self, name="Rax"):
        super().__init__(name)

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name="Stormy"):
        super().__init__(name)

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.adopted_pets = []

    def adopt_pet(self, pet):
        if not isinstance(pet, Animal):
            raise TypeError("pet must be an instance of the Animal class.")
        elif pet in self.adopted_pets:
            raise ValueError("You cannot adopt the same pet twice.")
        else:
            self.adopted_pets.append(pet)

        return len(self.adopted_pets)

    def make_all_sounds(self):
        return [pet.sound() for pet in self.adopted_pets]
