from BankAccount.Account import Account


class SavingsAccount(Account):
    def __init__(self, account_name: str, starting_balance: int, interest_rate: int):
        super().__init__(account_name, starting_balance, interest_rate)
