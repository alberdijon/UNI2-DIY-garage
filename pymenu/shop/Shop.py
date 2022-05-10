from importlib import import_module
import pickle

class Product:
    def __init__(self, id, name, price, stock, brand):
        self.id = int(id)
        self.name = str(name)
        self.price = int(price)
        self.stock = int(stock)
        self.brand = str(brand)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.price} - {self.stock} - {self.brand}"
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_stock(self):
        return self.stock
    def get_brand(self):
        return self.brand
    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_stock(self, stock):
        self.stock = stock
    def set_brand(self, brand):
        self.brand = brand
    
def Shop_menu():
    print("1. Add product")
    print("2. View all products")
    print("3. Change stock")
    print("4. Edit product")
    print("5. Remove product")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()
        Shop_menu()
    elif choice == "2":
        view_products()
        Shop_menu()
    elif choice == "3":
        stock_menu()
        Shop_menu()
    elif choice == "4":
        edit_product()
        Shop_menu()
    elif choice == "5":
        remove_product()
        Shop_menu()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice")
        Shop_menu()

def view_products():
    inp=open('Products.pkl','rb')
    objects = []
    cont=1
    while cont==1:
        try:
            objects.append(pickle.load(inp))
        except EOFError:
            print("end of products\n")
            cont=0
    for Product in objects:
      print(Product.id)
      print(Product.name)
      print(Product.price)
      print(Product.stock)
      print(Product.brand)
      cont=0

def stock_menu():
    print("1. Add stock to a product")
    print("2. Remove stock from a product")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_stock_to_product()
        stock_menu()
    elif choice == "2":
        remove_stock_from_product()
        stock_menu()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice")
        stock_menu()

def add_stock_to_product():
    view_products()
    inp=open('Products.pkl','rb')
    objects = []
    cont=1
    while cont==1:
        try:
            objects.append(pickle.load(inp))
        except EOFError:
            print("end of products\n")
            cont=0
    product_to_edit = int(input("Enter the id of the product you want to add stock: "))
    for Product in objects:
        the_id = int(Product.id)
        if the_id == product_to_edit:
            print("Product found")
            new_stock = input("Enter how much stock you want to add: ")
            Product.stock += new_stock
            with open('Products.pkl', 'wb') as inp:
                pickle.dump(objects, f)
            print("Stock added")

def remove_stock_from_product():
    try:
        with open("Products.pickle", "rb") as f:
            products = pickle.load(f)
    except EOFError:
        products = []
        print("No product in database")
    product_to_edit = input("Enter the id of the product you want to remove stock: ")
    for Product in products:
        if Product.id == product_to_edit:
            print("Product found")
            stock = input("Enter how much stock you want to remove: ")
            Product.stock -= stock
            with open("Products.pickle", "wb") as f:
                pickle.dump(products, f)
            print("Stock removed")
            Shop_menu()
    print("No product found with that id")

def edit_product():
    try:
        with open("Products.pickle", "rb") as f:
            products = pickle.load(f)
    except EOFError:
        products = []
        print("No product in database")
    product_to_edit = input("Enter the id of the product you want to edit: ")
    for Product in products:
        if Product.id == product_to_edit:
            print("Product found")
            id = input("Enter id: ")
            name = input("Enter name: ")
            price = input("Enter price: ")
            stock = input("Enter stock: ")
            brand= input("Enter brand: ")
            Product.first_name = id
            Product.last_name = name
            Product.email = price
            Product.password = stock
            Product.phone_number = brand
            with open("Products.pickle", "wb") as f:
                pickle.dump(products, f)
            print("Product edited")
            Shop_menu()
    print("No product found with that id")

def remove_product():
   with open("Products.pickle", "rb") as f:
        products = pickle.load(f)
   product_id = input("Enter the id of the product you want to delete: ")
   amount_deleted = 0
   for Product in products:
        if Product.id == product_id:
            print("A product has been deleted.")
            amount_deleted += 1
            products.remove(Product)
   with open("Products.pickle", "wb") as f:
        pickle.dump(products, f)
   if amount_deleted == 0:
        print("No product found with that id")
   else:
        print("Product deleted")

def add_product():
    id = input("Enter id: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    stock = input("Enter stock: ")
    brand = input("Enter brand: ")
    p1 = Product(id, name, price, stock, brand)
    with open('Products.pkl', 'ab') as f:
        pickle.dump(p1, f)
    print("Product added")

def exit_program():
    print("Thank you for using the program")

Shop_menu()