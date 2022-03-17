# ISP
from abc import abstractmethod


class Machine:  # Пример плохого интерфеса
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunction(Machine):
    def print(self, document):
        ...

    def fax(self, document):
        ...

    def scan(self, document):
        ...


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        ...

    def fax(self, document):
        ...  # noop

    def scan(self, document):
        """Not Supported!"""
        raise NotImplementedError("Printer cannot scan!")


# Пример хорошего интерфейса
class Printer:
    @abstractmethod
    def print(self, document):
        ...


class Scanner:
    @abstractmethod
    def scan(self, document):
        ...


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        ...

    def scan(self, document):
        ...


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        ...

    @abstractmethod
    def scan(self, document):
        ...


# class MultiFunctionMachine(MultiFunctionDevice):
#     def print(self, document):
#         ...
#
#     def scan(self, document):
#         ...

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
