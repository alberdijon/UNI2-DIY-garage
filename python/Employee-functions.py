import pickle

import Employee
from Employee import *


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
        ans = input("What would you like to do?")

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
            employee_menu()


def viewemployees():
    f = open('employees.pkl', 'rb')
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
    employee_menu()


def hire():
    ans = 'y'
    while ans == 'y':
        employee = Employee(employee.setid(), employee.setname(), employee.setsurname(), employee.setgmail(),
                            employee.setmobile(), employee.job, employee.setsalary())

        # Overwrites any existing file.
        with open('employees.pkl', 'ab') as f:
            pickle.dump(employee, f)
        print("Added succesfully")
        del employee
        ans = int(input("Do you want to add a new employee? (y/n)"))
    employee_menu()


def fire():

    f = open('employees.pkl', 'rb')
    employees = []
    cont = 1

    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0

    employee_to_delete = input("Enter the id of the employee you want to delete: ")
    for employee in employees:
        # hacer sin esto: e1 = Employee(employee.id, employee.name, employee.surname, employee.gmail, employee.mobile, employee.job,
        # employee.salary)
        try:
            if employee.id == employee_to_delete:

                with open("employees.pkl", "wb") as f:
                    pickle.dump(employee, f)
                    print("Deleted succesfully")

            else:
                with open("employees.pkl", "wb") as f:
                    pickle.dump(e1, f)
        except EOFError:

            print("no employee found")
    employee_menu()


def edit_employees():

    f = open('employees.pkl', 'rb')
    employees = []
    cont = 1
    while cont == 1:
        try:

            employees.append(pickle.load(f))

        except EOFError:

            cont = 0

    employee_to_edit = input("Enter the id of the employee you want to edit: ")

    for employee in employees:

        try:

            if employee.id == employee_to_edit:

                e1 = Employee(employee.setid(), employee.setname(), employee.setsurname(), employee.setgmail(),
                              employee.setmobile(), employee.job, employee.setsalary())
                with open("employees.pkl", "ab") as f:
                    pickle.dump(e1, f)
                print("employee edited")
            else:
                with open("employees.pkl", "wb") as f:
                    pickle.dump(employee, f)
        except EOFError:

            print("no employee found")
    employee_menu()


employee_menu()
