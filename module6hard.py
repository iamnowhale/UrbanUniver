class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        if self.__is_valid_sides(sides):
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count

        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [255, 255, 255]

        self.filled = filled

    def __is_valid_color(self, r, g, b):
        return (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled)
        self.__radius = sides[0] / 3.14 ** 0.5

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled)

    def get_square(self):
        p = len(self) / 2
        a = (p - self.__sides[0])
        b = (p - self.__sides[1])
        c = (p - self.__sides[2])
        square = (p * a * b * c) ** 0.5
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled)
        self.__sides = [sides[0]] * 12

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
