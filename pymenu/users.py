import pickle


class User:
    def __init__(self, first_name, last_name, email, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number


def users_menu():
    print("=============================")
    print("Welcome to the User Database")
    print("=============================")
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
    try:
        with open("users.pickle", "rb") as f:
            users = pickle.load(f)
    except EOFError:
        users = []
        print("No users in database")
    valid = True
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    for user in users:
        if user.email == email:
            print("Email already in use")
            print("Returning to main menu")
            valid = False
    if valid:
        password = input("Enter password: ")
        phone_number = input("Enter phone number: ")
        new_user = User(first_name, last_name, email, password, phone_number)
        users.append(new_user)
        with open("users.pickle", "wb") as f:
            pickle.dump(users, f)
        print("User added")
    users_menu()


def delete_user():
    with open("users.pickle", "rb") as f:
        users = pickle.load(f)
    user_to_delete = input("Enter the email of the user you want to delete: ")
    amount_deleted = 0
    for user in users:
        if user.email == user_to_delete:
            amount_deleted = amount_deleted + 1
            users.remove(user)
    with open("users.pickle", "wb") as f:
        pickle.dump(users, f)
    if amount_deleted == 0:
        print("No users found with that email")
    else:
        print("Deletion complete")
    users_menu()


def edit_user():
    try:
        with open("users.pickle", "rb") as f:
            users = pickle.load(f)
    except EOFError:
        users = []
        print("No users in database")
    user_to_edit = input("Enter the email of the user you want to edit: ")
    for user in users:
        if user.email == user_to_edit:
            print("User found")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone_number = input("Enter phone number: ")
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.password = password
            user.phone_number = phone_number
            with open("users.pickle", "wb") as f:
                pickle.dump(users, f)
            print("User edited")
            users_menu()
    print("No users found with that email")
    users_menu()


users_menu()
