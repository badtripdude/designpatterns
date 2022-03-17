# Open _ Closed Principle
'''
В этом примере демонстрируется, что идея принципа открытости-закрытости состоит в том,
что нужно избегать ситуации, когда вам придется менять код, который был протестирован и запущен в продакшн

Принцип открытости/закрытости Мейера
Полиморфный принцип открытости/закрытости - это лучше!
'''
# OCP = open for extension, closed for modification
# Таким образом, классы дожны быть открыты для расширения и закрыты для модификации
# https://webdevblog.ru/princip-otkrytosti-zakrytosti/
from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:  # Bad Trip
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        ...


# Specification

class Specification: # Base class
    def is_satisfied(self, item):
        ...

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        ...


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('apple', Color.GREEN, Size.BIG)
    lemon = Product('lemon', Color.GREEN, Size.BIG)
    mango = Product('mango', Color.BLUE, Size.SMALL)

    products = [apple, mango, lemon]

    pf = ProductFilter()
    bf = BetterFilter()

    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green!')

    print()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green!')

    print('Big Products:')
    big = SizeSpecification(Size.BIG)
    for p in bf.filter(products, big):
        print(f' - {p.name} is BIG!')

    print('Big Green products:')
    # big_green = AndSpecification(big, green)
    big_green = big & green

    for p in bf.filter(products, big_green):
        print(f' - {p.name} is BIG and GREEN!')
