from Employee.Employee import Employee


class Engineer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 5000

    def __str__(self):
        return "Engineer: " + self.name + "\nSalary: " + str(self.get_salary()) + " dollars"

    def WriteCode(self, algorithm_name):
        print(self.name + " is writing " + algorithm_name + " algorithm")

    def TestCode(self, algorithm_name):
        print(self.name + " is testing " + algorithm_name + " algorithm")
