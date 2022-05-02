import pickle
import Employees

def viewemployees():

    inp=open('employees_data.pkl','rb')
    employees = []
    cont=1

    while cont==1:
        try:
            employees.append(pickle.load(inp))

        except EOFError:
            print ('end of employees')
            cont=0

    for emp in employees:
        print(emp)


def viewemployeesworking():
    inp = open('employees_data.pkl', 'rb')
    employees = []
    cont = 1

    while cont == 1:
        try:

            employees.append(pickle.load(inp))

        except EOFError:
            print('end of employees')
            cont = 0

    for emp in employees:
        print(emp)


def hire(obj, filename):
    with open(filename, 'ab') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    ans = 1
    while ans == 1:
        e1 = Employees.Employees()
        # sample usage
        hire(e1, 'employees_data.pkl')
        ans = int(input("Do you want to add a new student? (1/0)"))

    del e1


