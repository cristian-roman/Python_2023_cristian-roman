class Account:
    def __init__(self, name: str, starting_balance: int, interest_rate: int):
        self.__name = name
        self.__balance = starting_balance
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful. Balance is now: " + str(self.__balance) + " dollars")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print("Withdrawal successful. Balance is now: " + str(self.__balance) + " dollars")

    def add_interest_to_balance(self):
        self.__balance += self.__balance * self.__interest_rate / 100
        print("Interest added to balance. Balance is now: " + str(self.__balance) + " dollars")

    def set_interest_rate(self, rate):
        print("Interest rate changed. From " + str(self.__interest_rate) + " to " + str(rate))
        self.__interest_rate = rate

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Name: " + self.__name + "\nBalance: " + str(self.__balance)
