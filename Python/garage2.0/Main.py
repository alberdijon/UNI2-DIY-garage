from CabinMethods import *
from UserMethods import *
from ShopMethods import *
from EmployeeMethods import *

class Main:
    
    def main_menu():
        print("1. users")
        print("2. employees")
        print("3. cabins")
        print("4. shop")
        print("5. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            UserMethods.users_menu()
        elif choice == "2":
            EmployeeMethods.employee_menu()
        elif choice == "3":
            CabinMethods.menu_cabins()
        elif choice == "4":
            ShopMethods.Shop_menu()
        elif choice == "5":
            print("Good Bye!")
        else:
            print("Invalid choice")


    main_menu()