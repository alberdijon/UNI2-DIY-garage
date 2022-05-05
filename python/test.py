
from Employee import *


def hire(obj, filename):
    with open(filename, 'ab') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


ans = 1
while ans == 1:
    e1 = Employees.Employees()
    # sample usage
    hire(e1, 'employees.txt')
    ans = int(input("Do you want to add a new student? (1/0)"))

del e1
