class Users:
    def __init__(self, password, email, first_name, last_name, tlf):
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.tlf = tlf

def users_menu():
    print("Welcome to the User Database")
    print("1. View Users")
    print("2. Add User")
    print("3. Delete User")
    print("4. Edit User")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_users()
    elif choice == "2":
        add_user()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        edit_user()
    elif choice == "5":
        exit_program()
    else:
        print("Invalid choice")
        users_menu()


def view_users():
    with open("users.txt", "r") as file:
        for line in file:
            p1 = Users(line.split(","))
            print(p1)
    users_menu()

def add_user():
    with open("users.txt", "a") as file:
        p1 = Users
        p1.password = input("Enter password: ")
        p1.email = input("Enter email: ")
        p1.first_name = input("Enter first name: ")
        p1.last_name = input("Enter last name: ")
        p1.tlf = input("Enter tlf: ")
        file.write(p1.password + "," + p1.email + "," + p1.first_name + "," + p1.last_name + "," + p1.tlf + "\n")
    users_menu()

def delete_user():
    with open("users.txt", "r") as f:
        lines = f.readlines()
    email = input("Enter email: ")
    with open("users.txt", "w") as f:
     for line in lines:
        if line.strip("\n") != email:
            f.write(line)
    users_menu()

def edit_user():
    with open("users.txt", "r") as file:
        for line in file:
          print(line)
    email = input("Enter email: ")
    with open("users.txt", "r") as file:
        for line in file:
            if email in line:
                password = input("Enter password: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                tlf = input("Enter tlf: ")
                line = line.replace(password, password)
                line = line.replace(first_name, first_name)
                line = line.replace(last_name, last_name)
                line = line.replace(tlf, tlf)
            else:
                print("Email not found")
    users_menu()











    string1 = input("Enter the user's you want to search for: ")
    file1 = open("users.txt")
    list_of_lines = [file1.readlines()]
    flag = 0
    for line in file1:
        index = index+1
        if string1 in line:
            flag = 1
            break
    if flag == 0:
        print('User', string1, 'Not Found')
    else:
         p1 = Users(string1.split(","))
         print(p1)
         print("You want to change just a part of the user's information? (y/n)")
         choice = input()
         if choice == "y":
            print("wich part of the user's information do you want to change?")
            choice2=input()
            print("Enter the new information")
            if choice2 == "password":
                p1.password = input()
            elif choice2 == "email":
                p1.email = input()
            elif choice2 == "first_name":
                p1.first_name = input()
            elif choice2 == "last_name":
                p1.last_name = input()
            elif choice2 == "tlf":
                p1.tlf = input()
            else:
                print("Invalid choice")
            list_of_lines[index-1] = p1.password + "," + p1.email + "," + p1.first_name + "," + p1.last_name + "," + p1.tlf + "\n"
            file1.writelines(list_of_lines)
         else:
            p1.password = input("Enter password: ")
            p1.email = input("Enter email: ")
            p1.first_name = input("Enter first name: ")
            p1.last_name = input("Enter last name: ")
            p1.tlf = input("Enter tlf: ")
            list_of_lines[index-1] = p1.password + "," + p1.email + "," + p1.first_name + "," + p1.last_name + "," + p1.tlf + "\n"
            file1.writelines(list_of_lines)
    file1.close()























def exit_program():
    print("Exiting program")

users_menu()



