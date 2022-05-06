from users import users_menu


def main_menu():
    choice = 0
    print("===============================")
    print("Welcome to the main menu")
    print("===============================")
    print("1. users")
    print("2. employees")
    print("3. cabins")
    print("4. shop")
    print("0. EXIT")
    choice = input("Enter your choice: ")
    if choice == "1":
        users_menu()
    elif choice == "2":
        employees_menu()
    elif choice == "3":
        cabins_menu()
    elif choice == "4":
        shop_menu()
    elif choice == "0":
        print("Bye!")
        print("designed by uni2")
        exit()
    else:
        print("Invalid choice")
        main_menu()


main_menu()
