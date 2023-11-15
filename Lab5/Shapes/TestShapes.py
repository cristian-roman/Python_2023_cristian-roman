from Shapes.Circle import Circle
from Shapes.Rectangle import Rectangle
from Shapes.Triangle import Triangle


class TestShapes:
    @staticmethod
    def test_shapes():
        shapes = [Circle(5), Rectangle(5, 10), Triangle(3, 4, 5)]
        for shape in shapes:
            print(f"Area of \"{shape.__class__.__name__}\" is {shape.get_area()}")
            print(f"Perimeter of \"{shape.__class__.__name__}\" is {shape.get_perimeter()}")
            print()
