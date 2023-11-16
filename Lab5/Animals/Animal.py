class Animal:
    def __init__(self, name):
        self.name = name

    def type(self):
        raise NotImplemented

    def give_birth(self):
        raise NotImplemented

    def move(self):
        raise NotImplemented
