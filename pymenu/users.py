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
    # Open the users.pkl file
    with open("users.pkl", "rb") as f:
        pklusers = pickle.load(f)
    # Print the users
    for user in pklusers:
        print(user)
    users_menu()


def add_user():
    # create a new user
    new_user = User(input("Enter your first name: "), input("Enter your last name: "), input("Enter your email: "), input("Enter your password: "), input("Enter your phone number: "))
    # Open the users.pkl file
    with open("users.pkl", "rb") as f:
        pklusers = pickle.load(f)
    # Add the new user to the list
    pklusers.append(new_user)
    # Save the list to the users.pkl file
    with open("users.pkl", "wb") as f:
        pickle.dump(pklusers, f)
    print("User added")
    users_menu()


users_menu()
