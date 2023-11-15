from BankAccount.Account import Account


class CheckingAccount(Account):
    withdraw_fee = 1.5

    def __init__(self, account_name: str, starting_balance: int):
        super().__init__(account_name, starting_balance)
        self.epoch = 0

    def withdraw(self, amount):
        self.epoch += 1
        amount += self.withdraw_fee * self.get_interest()
        super().withdraw(amount)

    def deposit(self, amount):
        self.epoch += 1
        super().deposit(amount)

    def get_interest(self):
        if self.epoch < 0:
            return 1
        elif self.epoch < 2:
            return 1.2
        elif self.epoch < 4:
            return 1.4
        else:
            return 2
