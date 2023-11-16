from Employee.Employee import Employee


class Salesperson(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 12000

    def __str__(self):
        return "Salesperson: " + self.name + "\nSalary: " + str(self.get_salary()) + " dollars"

    def Sell(self, saleObject):
        print(self.name + " is selling: " + saleObject)

    def CreateOffer(self, offerObject):
        print(self.name + " is creating offer: " + offerObject)
