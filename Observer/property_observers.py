class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if self._age == val:
            return
        self._age = val
        self.property_changed('age', val)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, val):
        if name == 'age':
            if val < 16:
                print('Sorry, but you still can not drive')
            else:
                print('Okey, you can drive now!')
                self.person.property_changed.remove(self.person_changed)


if __name__ == '__main__':
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age

