from BankAccount.SavingsAccount import SavingsAccount
from BankAccount.CheckingAccount import CheckingAccount


class TestAccount:

    @staticmethod
    def test_savings_account():
        account = SavingsAccount("Savings Test Account", 1000, 1)
        print(account)
        account.deposit(100)
        assert account.get_balance() == 1100

        account.withdraw(100)
        assert account.get_balance() == 1000

        print("A year has passed...")
        account.add_interest_to_balance()
        assert account.get_balance() == 1010

        account.set_interest_rate(2)
        print("Another year has passed and interest rate is bigger...")
        account.add_interest_to_balance()
        assert account.get_balance() == 1030.2

        print()

    @staticmethod
    def test_checking_account():
        account = CheckingAccount("Checking Test Account", 1000)
        print(account)

        account.deposit(100)
        assert account.get_balance() == 1100

        account.withdraw(100)
        assert account.get_balance() == 1000

        print("A year has passed...")
        account.add_interest_to_balance()
        assert account.get_balance() == 1000
        account.set_interest_rate(0.5)
        print("Another year has passed and interest rate is bigger...")
        account.add_interest_to_balance()
        assert account.get_balance() == 1005
