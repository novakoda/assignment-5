# James Williams
import random

class InvalidValueError(ValueError):
    def __init__(self, salary):
        super().__init__()
        self.salary = salary

class Person:
    def __init__(self, firstname, lastname):
        self.__first_name = firstname
        self.__last_name = lastname

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, firstname):
        self.__first_name = firstname
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, lastname):
        self.__last_name = lastname
    def get_name(self):
        return self.get_first_name() + " " + self.get_last_name()

class Customer(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.__customer_id = ""
        self.__customer_email = ""
    def get_customer_id(self):
        return self.__customer_id
    def set_customer_id(self, custid):
        self.__customer_id = custid
    def get_customer_email(self):
        return self.__customer_email
    def set_customer_email(self, email):
        self.__customer_email = email
    def get_customer_info(self):
        return self.get_name() + ", " + self.get_customer_email()

class Employee(Person):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        self.emp_id = ""
        self.emp_salary = 0.0

    def set_emp_id(self):
        self.emp_id = random.randint(0,12342)
    def get_emp_id(self):
        return self.emp_id
    def set_emp_salary(self, salary):
        if (salary < 20000):
            raise InvalidValueError(salary)
        else:
            self.emp_salary = salary

    def get_emp_salary(self):
        return self.emp_salary
    def calculate_bonus(self):
        return self.emp_salary * 0.20

    
    












        
