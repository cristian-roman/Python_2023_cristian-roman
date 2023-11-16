from Employee.Employee import Employee


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 1000000

    def __str__(self):
        return "Manager: " + self.name + "\nSalary: " + str(self.get_salary()) + " dollars"

    def PostAnnouncement(self, announcement):
        print("Announcement from " + self.name + ": " + announcement)

    def Hire(self, employee):
        print(self.name + " is hiring: " + employee.name)
