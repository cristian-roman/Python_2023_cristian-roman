from Animals.Animal import Animal


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return "Bird"

    def give_birth(self):
        print(self.name + " is laying eggs")

    def move(self):
        print(self.name + " is flying")

    def __str__(self):
        return "Bird: " + self.name
