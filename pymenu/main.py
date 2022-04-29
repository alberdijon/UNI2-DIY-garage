from Users import *


def main_menu():
    print("1. users")
    print("2. employees")
    print("3. cabins")
    print("4. shop")
    print("5. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        users_menu()
    elif choice == "2":
        employees_menu()
    elif choice == "3":
        cabins_menu()
    elif choice == "4":
        employees_menu()
    elif choice == "5":
        shop_menu()
    else:
        print("Invalid choice")
        main_menu()


main_menu()
