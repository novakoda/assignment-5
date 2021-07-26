# James Williams
from customer import *

def create_employee():
    print("-+-+-+-+-\n\nCreating a new employee.....\n")
    first = input("First name: ")
    last = input("Last name: ")
    emp = Employee(first, last)
    try:
        salary = float(input("Enter the salary for %s: " % emp.get_name().title()))
        emp.set_emp_salary(salary)
        print("%s makes $%.2f/year salary with a $%.2f bonus" % (emp.get_name().title(), emp.get_emp_salary(), emp.calculate_bonus()))
        return emp
    except InvalidValueError as err:
        print("$%.2f/year is too low for a good employee!"%err.salary)

create_employee()
