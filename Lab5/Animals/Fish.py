from Animals.Animal import Animal

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return "Fish"

    def give_birth(self):
        print(self.name + " is laying eggs")

    def move(self):
        print(self.name + " is swimming")

    def jump(self):
        print(self.name + " is jumping from water")

    def __str__(self):
        return "Fish: " + self.name