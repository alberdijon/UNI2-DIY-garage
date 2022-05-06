import pickle

class Product:
    def __init__(self, id, name, price, stock, brand):
        self.id = set
        self.name = name
        self.price = price
        self.stock = stock
        self.brand = brand


def Shop_menu():
    print("1. Add product")
    print("2. View all products")
    print("3. Add stock")
    print("4. Edit product")
    print("5. Remove product")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        stock_menu()
    elif choice == "4":
        edit_product()
    elif choice == "5":
        remove_product()
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
    Shop_menu()

def stock_menu():
    print("1. Add stock to a product")
    print("2. Remove stock from a product")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_stock_to_product()
    elif choice == "2":
        remove_stock_from_product()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice")
        stock_menu()
    Shop_menu()

def add_stock_to_product():
    try:
        with open("Products.pickle", "rb") as f:
            products = pickle.load(f)
    except EOFError:
        products = []
        print("No product in database")
    product_to_edit = input("Enter the id of the product you want to add stock: ")
    for Product in products:
        if Product.id == product_to_edit:
            print("Product found")
            stock = input("Enter how much stock you want to add: ")
            Product.stock += stock
            with open("Products.pickle", "wb") as f:
                pickle.dump(products, f)
            print("Stock added")
            Shop_menu()
    print("No product found with that id")

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
    Shop_menu()

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
    Shop_menu()

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
   Shop_menu()

def add_product():
    id = input("Enter id: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    stock = input("Enter stock: ")
    brand = input("Enter brand: ")
    p1 = Product(id, name, price, stock, brand)
    products = []
   # try:
       # with open('Products.pkl', 'wb') as f:
        #    products.append( pickle.load(f))
    #except EOFError:
     #   products = []*/
    #1
    # products.append(Product)
    with open('Products.pkl', 'ab') as f:
        pickle.dump(p1, f)
    print("Product added")
    Shop_menu()

def exit_program():
    print("Thank you for using the program")
    exit()

Shop_menu()