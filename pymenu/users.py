class users:
    def __init__(self, first_name, last_name, email, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number


def users_menu():
    print("Welcome to the User Database")
    print("1. View Users")
    print("2. Add User")
    print("3. Delete User")
    print("4. Edit User")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_users()
    elif choice == "2":
        add_user()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        edit_user()
    elif choice == "0":
        print("Returning to main menu")
    else:
        print("Invalid choice")
        users_menu()


def view_users():
    with open("users.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip("\n"))
    users_menu()


def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone_number = input("Enter phone number: ")
    user = users(first_name, last_name, email, password, phone_number)
    with open("users.txt", "a") as f:
        f.write(f"{user.first_name} {user.last_name} {user.email} {user.password} {user.phone_number}\n")
    users_menu()


def delete_user():
    email = input("Enter email: ")
    with open("users.txt", "r") as f:
        lines = f.readlines()
    with open("users.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != email:
                f.write(line)
    users_menu()


users_menu()
