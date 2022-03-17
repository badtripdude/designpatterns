from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, '
              f'balance = {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, '
                  f'balance = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def invoke(self):
        ...

    def undo(self):
        ...


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposite(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposite(self.amount)


if __name__ == '__main__':
    ba = BankAccount()  # 0
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 100000
    )
    cmd.invoke()
    cmd.undo()



