from copy import deepcopy


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('123 London Road', 'London', 'UK'))

jane = deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '124 London Road'

print(jane)
print(john)
