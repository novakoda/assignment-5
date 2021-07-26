# James Williams
class InvalidValueError(ValueError):
    def __init__(self, salary):
        super().__init__()
        self.salary = salary

class Employee:
    def __init__(self):
        self.__name = ""
        self.__designation = ""
        self.__salary = 0

    def set_name(self, name):
        self.__name = name.lower()

    def set_designation(self, designation):
        self.__designation = designation.lower()

    def set_salary(self, salary):
        if (salary < 20000):
            raise InvalidValueError(salary)
        else:
            self.__salary = salary

    def get_name(self):
        return self.__name

    def get_designation(self):
        return self.__designation

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        bonus = 0
        if self.__designation.lower() == "director":
            bonus = self.__salary * .1
        elif self.__designation.lower() == "manager":
            bonus = self.__salary * .15
        elif self.__designation.lower() == "staff":
            bonus = self.__salary * .2
        return bonus

    def total_salary(self):
        return self.__salary + self.get_bonus()

    def info(self):
        return "\n------\nEmployee: %s\t  |  %s\nSalary: %.0f/year\t  |  Bonus: %.0f\t  |  Total Salary: %.0f/year\n------\n" % (
            self.__name.title(), self.__designation.capitalize(),
            self.__salary, self.get_bonus(), self.total_salary())
