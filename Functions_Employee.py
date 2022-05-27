import pickle
import os
from Employee import Employee

class Functions_Employee:

    def saveEmployee(self,obj, filename):
        with open(filename, 'ab') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    def Employees_menu(self):
        print("\n")
        print("Employees Menu -->")
        print("----------------")
        print("1. Hire Employee")
        print("2. View all Employee")
        print("3. Edit Employee")
        print("4. Fire Employee")
        print("0. Exit")
        print("\n")
        employee_choice = input("Enter your choice: ")
        print("\n")
        return  employee_choice


    def Hire(self):
        p1 = Employee()
        p1.setId()
        p1.setName()
        p1.setLastName()
        p1.setEmail()
        p1.getPhoneNumber()
        p1.set_job()
        p1.set_salary()
        p1.print()
        function_Employee = Functions_Employee()
        function_Employee.saveEmployee(p1, 'Employees.pkl')

    def Fire(self):
        if os.path.exists('Employees.pkl'):
            function_Employee = Functions_Employee()
            function_Employee.view_Employee()
            EmployeeID = input("Enter the id of the employee: ")
            inp = open('Employees.pkl', 'rb')
            Employees = []
            cont = 1
            while cont == 1:
                try:
                    Employees.append(pickle.load(inp))
                except EOFError:
                    print("end of Employees\n")
                    cont = 0
            inp.close()
            if os.path.exists('Employees.pkl'):
                os.remove('Employees.pkl')
            for cl in Employees:
                if int(cl.id) != int(EmployeeID):
                    function_Employee.saveEmployee(cl, 'Employees.pkl')
        else:
            print("There aren't any Employee")

    def view_Employee(self):
        if os.path.exists('Employees.pkl'):
            inp = open('Employees.pkl', 'rb')
            Employees = []
            cont = 1
            while cont == 1:
                try:
                    Employees.append(pickle.load(inp))
                except EOFError:
                    print("end of Employees\n")
                    cont = 0
            for c1 in Employees:
                c1 = Employee()
                c1.print()
        else:
            print("There aren't any employees")

    def edit_Employee(self):
        print("Modifying employee")
        if os.path.exists('Employees.pkl'):
            function_Employee = Functions_Employee()
            function_Employee.view_Employee()
            employeeID = input("Enter the id of the employee: ")
            inp = open('Employees.pkl', 'rb')
            employees = []
            cont = 1
            while cont == 1:
                try:
                    employees.append(pickle.load(inp))
                except EOFError:
                    cont = 0
            inp.close()
            if os.path.exists('Employees.pkl'):
                os.remove('Employees.pkl')
            for cl in employees:
                if int(cl.id) != int(employeeID):
                    function_Employee.saveEmployee(cl, 'Employees.pkl')
                elif int(cl.id) == int(employeeID):
                    p1 = Employee()
                    p1.setIdWP(employeeID)
                    p1.setName()
                    p1.setLastName()
                    p1.setEmail()
                    p1.setPhoneNumber()
                    p1.set_job()
                    function_Employee.Hire(p1, 'Employees.pkl')
                else:
                    print("There isn't any employee with the same id ")
        else:
            print("There aren't any employee")
