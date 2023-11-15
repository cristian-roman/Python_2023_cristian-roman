from Shapes.Shape import Shape


class Circle(Shape):

    def __init__(self, radius: int):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius
