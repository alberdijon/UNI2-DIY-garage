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
        print("\n")

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
    first_object = objects[0] 
    for product in objects:
        the_id = int(product.id)
        p1 = Product(product.id, product.name, product.price, product.stock, product.brand)
        try:
            if  the_id == first_object.id:
                print("Product found")
                new_stock = int(input("Enter how much stock you want to add: "))
                the_stock = int(product.stock)
                the_stock += new_stock
                p1.stock = the_stock
                with open('Products.pkl', 'wb') as f:
                    pickle.dump(p1, f)
                print("Stock added")
            elif the_id == product_to_edit:
                print("Product found")
                new_stock = int(input("Enter how much stock you want to add: "))
                the_stock = int(product.stock)
                the_stock += new_stock
                p1.stock = the_stock
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
                print("Stock added")
            else:
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
        except EOFError:
            print("No product found with that id")

def remove_stock_from_product():
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
    product_to_edit = int(input("Enter the id of the product you want to reduce stock: "))
    first_object = objects[0] 
    for product in objects:
        the_id = int(product.id)
        p1 = Product(product.id, product.name, product.price, product.stock, product.brand)
        try:
            if  the_id == first_object.id:
                print("Product found")
                new_stock = int(input("Enter how much stock you reduce to reduce: "))
                the_stock = int(product.stock)
                the_stock -= new_stock
                p1.stock = the_stock
                with open('Products.pkl', 'wb') as f:
                    pickle.dump(p1, f)
                print("Stock reduced")
            elif the_id == product_to_edit:
                print("Product found")
                new_stock = int(input("Enter how much stock you want to reduce: "))
                the_stock = int(product.stock)
                the_stock -= new_stock
                p1.stock = the_stock
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
                print("Stock reduce")
            else:
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
        except EOFError:
            print("No product found with that id")

def edit_product():
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
    product_to_edit = int(input("Enter the id of the product you want to edit: "))
    first_object = objects[0] 
    for product in objects:
        the_id = int(product.id)
        p1 = Product(product.id, product.name, product.price, product.stock, product.brand)
        try:
            if  the_id == first_object.id:
                print("Product found")
                id = input("Enter id: ")
                name = input("Enter name: ")
                price = input("Enter price: ")
                stock = input("Enter stock: ")
                brand = input("Enter brand: ")
                p1 = Product(id, name, price, stock, brand)
                with open('Products.pkl', 'wb') as f:
                    pickle.dump(p1, f)
                print("Product edited")
            elif the_id == product_to_edit:
                print("Product found")
                id = input("Enter id: ")
                name = input("Enter name: ")
                price = input("Enter price: ")
                stock = input("Enter stock: ")
                brand = input("Enter brand: ")
                p1 = Product(id, name, price, stock, brand)
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
                print("Product edited")
            else:
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
        except EOFError:
            print("No product found with that id")

def remove_product():
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
    product_to_delete = int(input("Enter the id of the product you want to delete: "))
    first_object = objects[0] 
    contt =0
    is_the_first = 0
    for product in objects:
        the_id = int(product.id)
        p1 = Product(product.id, product.name, product.price, product.stock, product.brand)
        try:
            if  product_to_delete == first_object.id and is_the_first == 1:
                with open('Products.pkl', 'wb') as f:  
                    pickle.dump(p1, f)
            elif product_to_delete != first_object.id and contt == 0:
                with open('Products.pkl', 'wb') as f:
                    pickle.dump(p1, f)
                contt =1
                is_the_first = 1
            elif the_id == product_to_delete and contt == 0:
                contt =1 
                print("Product deleted")
            elif the_id == product_to_delete and contt == 1:
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
                print("Product deleted")
            else:
                with open('Products.pkl', 'ab') as f:
                    pickle.dump(p1, f)
        except EOFError:
            print("No product found with that id")


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

