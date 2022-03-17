class Person:
    def __init__(self):
        # adress
        self.street_address = None
        self.post_index = None
        self.city = None
        # employment
        self.company_name = None
        self.postion = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.post_index}, {self.city}' \
               f'Employed at {self.company_name} as {self.postion} earning {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.postion = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self
import sched

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.post_index = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb \
        .lives\
            .at('123 LondonRoad')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print(person)
