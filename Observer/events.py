class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name
        self.falls_ill = Event()  # some event that someone can subscribe to

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')


if __name__ == '__main__':
    person = Person("Sherlock", '221B Baker St')

    # bind to events
    person.falls_ill.append(lambda name, addr: print(f"{name} is ill"))
    person.falls_ill.append(call_doctor)

    # trigger event
    person.catch_a_cold()

    # unbind from events
    person.falls_ill.remove(call_doctor)

    person.catch_a_cold()
