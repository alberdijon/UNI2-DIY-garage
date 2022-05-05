import pickle


class User:
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
    with open("users.pickle", "rb") as f:
        try:
            users = pickle.load(f)
        except EOFError:
            print("No users in database")
            users = []
    for user in users:
        print(user.first_name, user.last_name, user.email, user.password, user.phone_number)
    users_menu()


def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone_number = input("Enter phone number: ")
    user = User(first_name, last_name, email, password, phone_number)
    try:
        with open("users.pickle", "rb") as f:
            users = pickle.load(f)
    except EOFError:
        users = []
    users.append(user)
    with open("users.pickle", "wb") as f:
        pickle.dump(users, f)
    users_menu()


def delete_user():
    with open("users.pickle", "rb") as f:
        users = pickle.load(f)
    user_to_delete = input("Enter the email of the user you want to delete: ")
    for user in users:
        if user.email == user_to_delete:
            users.remove(user)
    with open("users.pickle", "wb") as f:
        pickle.dump(users, f)
    users_menu()


users_menu()
