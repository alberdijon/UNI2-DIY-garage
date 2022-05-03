class Products:
    def __init__(self, id, name, price, stock, brand):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.brand = brand
    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.stock}, {self.brand}"
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_stock(self):
        return self.stock
    def set_stock(self, stock):
        self.stock = stock
    def get_brand(self):
        return self.brand
    def set_brand(self, brand):
        self.brand = brand

def Shop_menu():
    print("1. Add product")
    print("2. View all products")
    print("3. Add stock")
    print("4. Edit product")
    print("5. Remove product")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        add_stock()
    elif choice == "4":
        edit_product()
    elif choice == "5":
        remove_product()
    elif choice == "6":
        exit_program()
    else:
        print("Invalid choice")
        Shop_menu()

def view_products():
    with open("Products.pkl", "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip("\n"))
    Shop_menu()

def add_stock():
    with open("Products.pkl", "r") as f:
        lines = f.readlines()
    id = input("Enter id: ")
    amount = input("Enter amount: ")
    with open("Products.pkl", "w") as f:
        for line in lines:
            if line.strip("\n") != id:
                f.write(line)
            else:
                f.write(line.strip("\n") + "," + amount + "\n")
    Shop_menu()

def edit_product():
    with open("Products.pkl", "r") as file:
        for line in file:
            print(line)
    id = input("Enter id: ")
    with open("Products.pkl", "r") as file:
        for line in file:
            if id in line:
                name = input("Enter name: ")
                price = input("Enter price: ")
                stock = input("Enter stock: ")
                brand = input("Enter brand: ")
                with open("products.pkl", "w") as file:
                    file.write(id + "," + name + "," + price + "," + stock + "," + brand + "\n")
    Shop_menu()

def remove_product():
    with open("Products.pkl", "r") as f:
        lines = f.readlines()
    id = input("Enter id: ")
    with open("Products.pkl", "w") as f:
        for line in lines:
            if line.strip("\n") != id:
                f.write(line)
    Shop_menu()


def add_product():
    id = input("Enter id: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    stock = input("Enter stock: ")
    brand = input("Enter brand: ")
    p1 = Products(id, name, price, stock, brand)
    with open("Products.pkl", "a") as file:
        file.write(f"{p1.id}, {p1.name}, {p1.price}, {p1.stock}, {p1.brand}/n")
    Shop_menu()


def exit_program():
    print("Thank you for using the program")
    exit()

Shop_menu()