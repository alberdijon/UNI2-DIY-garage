def main():
    print("Welcome to the main menu!")
    print("Please choose an option:")
    print("1. Users")
    print("2. Employees")
    print("3. Cabins")
    print("4. Shop")
    print("0. Exit")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        users()
    elif input_option == "2":
        employees()
    elif input_option == "3":
        cabins()
    elif input_option == "4":
        shop()
    elif input_option == "0":
        exit()
    else:
        print("Invalid option")


def users():
    print("Welcome to the users menu!")
    print("Please choose an option:")
    print("1. View users")
    print("2. Add a user")
    print("3. Edit a user")
    print("4. Delete a user")
    print("0. Go back to the main menu")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        view_users()
    elif input_option == "2":
        add_user()
    elif input_option == "3":
        edit_user()
    elif input_option == "4":
        delete_user()
    elif input_option == "0":
        main()
    else:
        print("Invalid option")


def employees():
    print("Welcome to the employees menu!")
    print("Please choose an option:")
    print("1. View employees")
    print("2. View currently working employees")
    print("3. Hire an employee")
    print("4. Fire an employee")
    print("5. Edit an employee")
    print("6. Edit an employee's status")
    print("0. Go back to the main menu")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        view_employees()
    elif input_option == "2":
        view_working_employees()
    elif input_option == "3":
        hire_employee()
    elif input_option == "4":
        fire_employee()
    elif input_option == "5":
        edit_employee()
    elif input_option == "6":
        edit_employee_status()
    elif input_option == "0":
        main()
    else:
        print("Invalid option")


def cabins():
    print("Welcome to the cabins menu!")
    print("Please choose an option:")
    print("1. View cabins")
    print("2. View available cabins")
    print("3. Edit a cabin")
    print("4. Change a cabin's status")
    print("0. Go back to the main menu")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        view_cabins()
    elif input_option == "2":
        view_available_cabins()
    elif input_option == "3":
        edit_cabin()
    elif input_option == "4":
        change_cabin_status()
    elif input_option == "0":
        main()
    else:
        print("Invalid option")


def shop():
    print("Welcome to the shop menu!")
    print("Please choose an option:")
    print("1. View items")
    print("2. Add an item")
    print("3. Edit an item")
    print("4. Delete an item")
    print("5. View items sold today")
    print("6. View items sold this week")
    print("0. Go back to the main menu")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        view_items()
    elif input_option == "2":
        add_item()
    elif input_option == "3":
        edit_item()
    elif input_option == "4":
        delete_item()
    elif input_option == "5":
        view_items_sold_today()
    elif input_option == "6":
        view_items_sold_this_week()
    elif input_option == "0":
        main()
    else:
        print("Invalid option")

# These don't work yet


def view_users():
    users_file = open("users.txt", "r")
    print(users_file.read())
    users_file.close()
    input("Press enter to go back to the main menu")
    users()


def view_employees():
    employees_file = open("employees.txt", "r")
    print(employees_file.read())
    employees_file.close()
    input("Press enter to go back to the main menu")
    employees()


def view_cabins():
    cabins_file = open("cabins.txt", "r")
    print(cabins_file.read())
    cabins_file.close()
    input("Press enter to go back to the main menu")
    cabins()


def view_items():
    items_file = open("items.txt", "r")
    print(items_file.read())
    items_file.close()
    input("Press enter to go back to the main menu")
    shop()


main()
