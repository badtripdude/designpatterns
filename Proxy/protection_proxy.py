class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self): # Не будем менять этот метод и создадим proxy, чтобы не нарушить OCP
        print(f'Car is being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('driver is too young!')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    driver = Driver('John', 10)
    car = CarProxy(driver)
    car.drive()


if __name__ == '__main__':
    main()
