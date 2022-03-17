# DIP
# Этот принцип гласит, что в вашем коде высокоуровневые классы, модули не должны напрямую зависеть от низкоуровневых модулей,
# в место этого они дожны зависеть от абстракций. По сути вы должны зависеть от интерфейсов, а не от конкретных реализаций.
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        ...


class Relationships(RelationshipsBrowser):  # low-level
    # тк имеет дело с хранением
    def __init__(self):
        self.relations = []  # Мало ли мы сюда потом захочем привязать БД ?!

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module
    # def __init__(self, relationships): # Bad practice
    #     relation = relationships.relations
    #     for r in relation:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}.")

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
