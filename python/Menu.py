

from Employees import *

ans = True
while ans:
    print("""
    Menu > Employees
    1.View Employees
    2.Hire
    3.Fire
    4.Edit
    5.Change Employee Status
    7.Exit
    """)
    ans = input("What would you like to do?")

    if ans == "1":
        viewemployees()
    elif ans == "2":
        hire()
    elif ans == "3":
        fire()

    elif ans == "6":
        print("\n Goodbye")
    else:
        print("\n Not Valid Choice Try again")
