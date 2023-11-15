from Shapes.Shape import Shape


class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__()
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
