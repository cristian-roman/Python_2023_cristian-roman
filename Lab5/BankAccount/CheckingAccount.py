from BankAccount.Account import Account


class CheckingAccount(Account):
    def __init__(self, account_name: str, starting_balance: int, interest_rate: int = 0):
        super().__init__(account_name, starting_balance, interest_rate)
