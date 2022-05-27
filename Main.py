from Functions_Employee import Functions_Employee
from Functions_Product import Functions_Product
from Functions_User import Functions_User
from CabinMethods import CabinMethods
from BasicMethods import BasicMethods
option = 9
def main_menu():
    print("\n")
    print("Welcome to the main menu")
    print("1. Users")
    print("2. Employees")
    print("3. Cabins")
    print("4. Products")
    print("0. Exit")
    print("\n")

while option != 0:
    main_menu()
    option = int(input("Enter your choice: "))

    if int(option) == 1:
        user_choice = 9
        while int(user_choice) != 0:
            function_User = Functions_User()
            user_choice = function_User.Users_menu()
            if int(user_choice) == 1:
                function_User.add_User()
            elif int(user_choice) == 2:
                function_User.view_user()
            elif int(user_choice) == 3:
                function_User.edit_user()
            elif int(user_choice) == 4:
                function_User.remove_user()
            elif int(user_choice) == 0:
                print("Exiting")
            else:
                print("Invalid choice")
                user_choice = 9
    
    elif int(option) == 2:
        employee_choice = 9
        while int(employee_choice) != 0:
            Function_Employee = Functions_Employee()
            employee_choice = Function_Employee.Employees_menu()
            if int(employee_choice) == 1:
                Function_Employee.Hire()
            elif int(employee_choice) == 2:
                Function_Employee.view_Employee
            elif int(employee_choice) == 3:
                Function_Employee.edit_Employee()
            elif int(employee_choice) == 4:
                Function_Employee.Fire()
            elif int(employee_choice) == 0:
                print("Exiting")
            else:
                print("Invalid choice")
                employee_choice = 9

    elif int(option) == 3:
        cabins_choice = 9
        while int(cabins_choice) != 0:
            cabins_choice = CabinMethods()
            cabins_choice = CabinMethods.Cabins_menu()
            if int(cabins_choice) == 1:
                CabinMethods.add_cabins()
            elif int(cabins_choice) == 2:
                CabinMethods.view_cabins()
            elif int(cabins_choice) == 3:
                CabinMethods.available_cabins()
            elif int(cabins_choice) == 4:
                CabinMethods.condition_cabins()
            elif int(cabins_choice) == 0:
                print("Exiting")
            else:
                print("Invalid choice")
                cabins_choice = 9

    elif int(option) == 4:
        product_choice = 9
        while int(product_choice) != 0:
            functions_Product = Functions_Product()
            product_choice = functions_Product.Shop_menu()
            if int(product_choice) == 1:
                functions_Product.add_product()
            elif int(product_choice) == 2:
                functions_Product.view_products()
            elif int(product_choice) == 3:
                functions_Product.stock_menu()
            elif int(product_choice) == 4:
                functions_Product.edit_product()
            elif int(product_choice) == 5:
                functions_Product.remove_product()
            elif int(product_choice) == 0:
                print("Exiting")
            else:
                print("Invalid choice")
                product_choice = 9

if int(option) == 0:
    BasicMethods.exit_program()



