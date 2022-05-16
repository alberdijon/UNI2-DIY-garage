from User import *
from BasicMethods import *
import pickle


class UserMethods:

    def users_menu():
        print("Welcome to the User Database")
        print("1. View Users")
        print("2. Add User")
        print("3. Delete User")
        print("4. Edit User")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            UserMethods.view_users()
        elif choice == "2":
            UserMethods.add_user()
        elif choice == "3":
            UserMethods.delete_user()
        elif choice == "4":
            UserMethods.edit_user()
        elif choice == "0":
            print("Returning to main menu")
        else:
            print("Invalid choice")
            UserMethods.users_menu()

    def view_users():
        with open("Users.pkl", "rb") as f:
            try:
                users = pickle.load(f)
            except EOFError:
                print("No users in database")
                users = []
        for user in users:
            print(user.first_name, user.last_name, user.email,
                  user.password, user.phone_number)
        UserMethods.users_menu()

    def add_user():
        try:
            with open("Users.pkl", "rb") as f:
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
            new_user = User(first_name, last_name, email,
                            password, phone_number)
            users.append(new_user)
            with open("Users.pkl", "wb") as f:
                pickle.dump(users, f)
            print("User added")
        UserMethods.users_menu()

    def delete_user():
        with open("Users.pkl", "rb") as f:
            users = pickle.load(f)
        user_to_delete = input(
            "Enter the email of the user you want to delete: ")
        amount_deleted = 0
        for user in users:
            if user.email == user_to_delete:
                amount_deleted = amount_deleted + 1
                users.remove(user)
        with open("Users.pkl", "wb") as f:
            pickle.dump(users, f)
        if amount_deleted == 0:
            print("No users found with that email")
        else:
            print("Deletion complete")
        UserMethods.users_menu()

    def edit_user():
        try:
            with open("Users.pkl", "rb") as f:
                users = pickle.load(f)
        except EOFError:
            users = []
            print("No users in database")
        user_to_edit = BasicMethods.askString(
            "Enter the email of the user you want to edit: ")
        for user in users:
            if user.email == user_to_edit:
                print("User found")
                user = User(User.set_first_name(BasicMethods.askString("First name")), User.set_last_name(BasicMethods.askString("Last name")), User.set_email(
                    BasicMethods.askString("e-mail")), User.set_password(BasicMethods("Password")), User.set_phone_number(BasicMethods.askInteger("Phone number")))
            with open("Users.pkl", "wb") as f:
                pickle.dump(users, f)
            print("User edited")
            UserMethods.users_menu()
        print("No users found with that email")
        UserMethods.users_menu()
