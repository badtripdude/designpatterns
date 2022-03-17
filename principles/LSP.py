# LSP
"""
LSP в формуллировке Роберта Мартином и Барбарой Лисков:
"Функции, которые используют ссылки на базовые классы, должны иметь возможность использовать объекты производных классов, не зная об этом"

LSP в формуллировке Герба Саттерна и Андрея Александреску:
"Подкласс не дожен требовать от вызывающего кода больше чем базовый класс и
не должен предоставлять вызывающему коду меньше, чем базовый класс."
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'width = {self.width}, height = {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val


class Square(Rectangle): # класс который нарушает LSP
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, val):
        self._width = self._height = val

    @Rectangle.height.setter
    def height(self, val):
        self._width = self._height = val


def use_it(rc: Rectangle): # Сюда должен приходить любой другой наследник Rectangle, если код ломается, то LSP нарушен!
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected: {expected}, got {rc.area}")


if __name__ == '__main__':
    rc = Rectangle(2, 5)
    use_it(rc)

    # Ломаем LSP
    sq = Square(5)
    use_it(sq)