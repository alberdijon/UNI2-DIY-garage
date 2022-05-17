from Employee import *
import pickle
from BasicMethods import *
class EmployeeMethods:
    def employee_menu():
        ans = True
        while ans:
            print("""
            Menu > Employees
            1.View Employees
            2.Hire
            3.Fire
            4.Edit
            0.Exit
            """)
            ans = BasicMethods.askString("The option you want to choose")

            if ans == "1":
                viewemployees()
            elif ans == "2":
                hire()
            elif ans == "3":
                fire()
            elif ans == "4":
                edit_employees()
            elif ans == "0":
                exit()

            else:
                print("\n Not Valid Choice Try again")
                EmployeeMethods.employee_menu()


def viewemployees():
    f = open('Employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0
    for employee in employees:
        print(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
              employee.salary)
    EmployeeMethods.employee_menu()


def hire():
    ans = 'y'
    while ans == 'y':
        employee = Employee("", "", "", "", "", "", "")
        employee = Employee(employee.setid(), employee.setname(), employee.setsurname(), employee.setgmail(),employee.setmobile(), employee.job, employee.setsalary())

        # Overwrites any existing file.
        with open('Employees.pkl', 'ab') as f:
            pickle.dump(employee, f)
        print("Added succesfully")
        del employee
        ans = BasicMethods.askString("continue hiring (y/n)")
    EmployeeMethods.employee_menu()


def fire():
    f = open('Employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:
            employees.append(pickle.load(f))
        except EOFError:
            cont = 0
    employee_to_delete = BasicMethods.askString("ID for the employee you want to fire ")
    for employee in employees:
        try:
            if employee.id == employee_to_delete:
                employees.remove(employee)
                print("Deleted succesfully")
            else:
                with open("Employees.pkl", "wb") as f:
                    pickle.dump(employee, f)
        except EOFError:
            print("no employee found")
    EmployeeMethods.employee_menu()


def edit_employees():

    f = open('Employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0

    employee_to_edit = BasicMethods.askString("ID for the employee you want to edit ")

    for employee in employees:

        try:

            if employee.id == employee_to_edit:

                e1 = Employee(employee.setid(), employee.setname(), employee.setsurname(), employee.setgmail(),
                              employee.setmobile(), employee.job, employee.setsalary())
                with open("Employees.pkl", "ab") as f:
                    pickle.dump(e1, f)
                print("employee edited")
            else:
                with open("Employees.pkl", "wb") as f:
                    pickle.dump(employee, f)
        except EOFError:

            print("no employee found")
    EmployeeMethods.employee_menu()


