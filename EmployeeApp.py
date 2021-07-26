# James Williams
from Employee import *

def create_employee():
    print("-+-+-+-+-\n\nCreating a new employee.....\n")
    name = input("Enter a name for the employee: ")
    designation = input("Is %s a director, manager, or staff?: " % name.title())
    salary = float(input("Enter the salary for %s: " % name.title()))
    try: 
        e = Employee()
        e.set_name(name)
        e.set_designation(designation)
        e.set_salary(salary)
        print("%s" % e.info())
        return e
    except InvalidValueError as e:
        print("$%.2f/year is too low for a good employee!"%e.salary)

create_employee()
