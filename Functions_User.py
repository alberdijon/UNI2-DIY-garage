import pickle
import os
from User import User

class Functions_User:

    def saveUser(self,obj, filename):
        with open(filename, 'ab') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    def Users_menu(self):
        print("\n")
        print("User Menu -->")
        print("----------------")
        print("1. Add User")
        print("2. View all Users")
        print("3. Edit User")
        print("4. Remove User")
        print("0. Exit")
        print("\n")
        user_choice = int(input("Enter your choice: "))
        print("\n")
        return  user_choice


    def add_User():
        p1 = User()
        p1.id = p1.setId()
        p1.setName()
        p1.setLastName()
        p1.setEmail()
        p1.setPhoneNumber()
        p1.setPassword()
        p1.print()
        function_User = Functions_User()
        function_User.saveUser(p1, 'Users.pkl')

    def remove_user(self):
        if os.path.exists('Users.pkl'):
            function_User = Functions_User()
            function_User.view_user()
            userID = input("Enter the id of the user: ")
            inp = open('Users.pkl', 'rb')
            users = []
            cont = 1
            while cont == 1:
                try:
                    users.append(pickle.load(inp))
                except EOFError:
                    print("end of Users\n")
                    cont = 0
            inp.close()
            if os.path.exists('Users.pkl'):
                os.remove('Users.pkl')
            for cl in users:
                if int(cl.id) != int(userID):
                    function_User.saveUser(cl, 'Users.pkl')
        else:
            print("There aren't any users")

    def view_user(self):
        if os.path.exists('Users.pkl'):
            inp = open('Users.pkl', 'rb')
            users = []
            cont = 1
            while cont == 1:
                try:
                    users.append(pickle.load(inp))
                except EOFError:
                    print("end of users\n")
                    cont = 0
            for c1 in users:
                c1 = User()
                c1.print()
        else:
            print("There aren't any users")

    def edit_user(self):
        print("Modifying user")
        if os.path.exists('Users.pkl'):
            function_User = Functions_User()
            function_User.view_user()
            userID = input("Enter the id of the user: ")
            inp = open('Users.pkl', 'rb')
            users = []
            cont = 1
            while cont == 1:
                try:
                    users.append(pickle.load(inp))
                except EOFError:
                    cont = 0
            inp.close()
            if os.path.exists('Users.pkl'):
                os.remove('Users.pkl')
            for cl in users:
                if int(cl.id) != int(userID):
                    function_User.saveUser(cl, 'Users.pkl')
                elif int(cl.id) == int(userID):
                    p1 = User()
                    p1.setIdWP(userID)
                    p1.setName()
                    p1.setLastName()
                    p1.setEmail()
                    p1.setPhoneNumber()
                    p1.setPassword()
                    function_User.saveUser(p1, 'Users.pkl')
                else:
                    print("There isn't any user with the same id ")
        else:
            print("There aren't any user")
