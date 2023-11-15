class Account:
    def __init__(self, name: str, starting_balance: int):
        self.__name = name
        self.__balance = starting_balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful for account: " + self.__name + ". Balance is now: " + str(self.__balance) + " dollars")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Wanting to retrieve: " + str(amount) + ". Insufficient funds")
        else:
            self.__balance -= amount
            print("Withdrawal successful for account: " + self.__name + ". Balance is now: " + str(self.__balance) + " dollars")

    def get_interest(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_balance(self):
        return self.__balance

    def get_account_name(self):
        return self.__name

    def __str__(self):
        return "Name: " + self.__name + "\nBalance: " + str(self.__balance)
