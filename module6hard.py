class Figure:
    def __init__(self):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(x > 0 for x in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
        self.__sides = [2 * 3.14 * radius]

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c):
        super().__init__()
        self.__sides = [a, b, c]

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
class Cube(Figure):
    sides_count = 12

    def __init__(self, side):
        super().__init__()
        self.__sides = [side] * 12

    def get_volume(self):
        return self.__sides[0] ** 3