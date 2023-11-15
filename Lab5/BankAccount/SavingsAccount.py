from BankAccount.Account import Account


class SavingsAccount(Account):
    deposit_fee = 2

    def __init__(self, account_name: str, starting_balance: int):
        super().__init__(account_name, starting_balance)
        self.epoch = 0

    def deposit(self, amount):
        self.epoch += 1
        amount -= self.deposit_fee * self.get_interest()
        super().deposit(amount)

    def withdraw(self, amount):
        self.epoch -= 1
        super().withdraw(amount)

    def get_interest(self):
        if self.epoch < 0:
            if self.epoch < -2:
                return 1
            elif self.epoch < -4:
                return 1.2
            else:
                return 1.4
        else:
            if self.epoch < 2:
                return 0.5
            elif self.epoch < 4:
                return 0.2
            else:
                return 0.1
