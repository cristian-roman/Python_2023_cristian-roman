from BankAccount.SavingsAccount import SavingsAccount
from BankAccount.CheckingAccount import CheckingAccount


class TestAccount:

    @staticmethod
    def test_accounts():
        savings_account = SavingsAccount("Savings Account", 100)
        checking_account = CheckingAccount("Checking Account", 100)

        savings_account.deposit(100)
        savings_account.withdraw(100)
        savings_account.withdraw(100)

        checking_account.deposit(100)
        checking_account.withdraw(100)
        checking_account.withdraw(100)

        print(f"Balance of \"{savings_account.get_account_name()}\" is {savings_account.get_balance()}")
        print(f"Balance of \"{checking_account.get_account_name()}\" is {checking_account.get_balance()}")
        print()
