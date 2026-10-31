class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: ფართობი = {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height, name="მართკუთხედი"):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("სიგანე უნდა იყოს დადებითი")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("სიმაღლე უნდა იყოს დადებითი")
        self._height = value

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side, name="კვადრატი")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("წრე")
        if radius < 0:
            raise ValueError("რადიუსი უნდა იყოს დადებითი")
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2, 2)

def total_area(shapes):
    return round(sum(shape.area() for shape in shapes), 2)


def largest(shapes):
    if not shapes:
        return None
    largest_shape = max(shapes, key=lambda s: s.area())
    return largest_shape.name

shapes = [
    Rectangle(4, 5),
    Square(3),
    Circle(2),
    Shape("უცნობი ფიგურა")
]

for shape in shapes:
    shape.info()

print(f"ჯამური ფართობი: {total_area(shapes)}")
print(f"უდიდესი: {largest(shapes)}")


rect_count = sum(1 for shape in shapes if isinstance(shape, Rectangle))
print(f"მართკუთხედების რაოდენობა (კვადრატის ჩათვლით): {rect_count}")

try:
    Circle(-3)
except ValueError as e:
    print(f"შეცდომა: {e}")

try:
    Square(0)
except ValueError as e:
    print(f"შეცდომა: {e}")