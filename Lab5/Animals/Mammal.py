from Animals.Animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return "Mammal"

    def give_birth(self):
        print(self.name + " is giving birth to a mammal")

    def feed(self):
        print(self.name + " is feeding its baby")

    def move(self):
        print(self.name + " is walking")

    def __str__(self):
        return "Mammal: " + self.name
