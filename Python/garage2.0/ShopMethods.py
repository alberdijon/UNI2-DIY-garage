from BasicMethods import BasicMethods
from Product import *
import pickle

class ShopMethods:

    def shop_menu():
        print("1. Add product")
        print("2. View all products")
        print("3. Change stock")
        print("4. Edit product")
        print("5. Remove product")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            ShopMethods.add_product()
            ShopMethods.Shop_menu()
        elif choice == "2":
            ShopMethods.view_products()
            ShopMethods.Shop_menu()
        elif choice == "3":
            ShopMethods.stock_menu()
            ShopMethods.Shop_menu()
        elif choice == "4":
            ShopMethods.edit_product()
            ShopMethods.Shop_menu()
        elif choice == "5":
            ShopMethods.remove_product()
            ShopMethods.Shop_menu()
        elif choice == "0":
            print("Good Bye!")
        else:
            print("Invalid choice")
            ShopMethods.Shop_menu()

    def view_products():
        inp = open('Products.pkl', 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                print("end of products\n")
                cont = 0
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
            ShopMethods.add_stock_to_product()
            ShopMethods.stock_menu()
        elif choice == "2":
            ShopMethods.remove_stock_from_product()
            ShopMethods.stock_menu()
        elif choice == "0":
            ShopMethods.exit_program()
        else:
            print("Invalid choice")
            ShopMethods.stock_menu()

    def add_stock_to_product():
        ShopMethods.view_products()
        inp = open('Products.pkl', 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                print("end of products\n")
                cont = 0
        product_to_edit = int(
            input("Enter the id of the product you want to add stock: "))
        first_object = objects[0]
        for product in objects:
            the_id = int(product.id)
            p1 = Product(product.id, product.name, product.price,
                         product.stock, product.brand)
            try:
                if the_id == first_object.id:
                    print("Product found")
                    new_stock = int(
                        input("Enter how much stock you want to add: "))
                    the_stock = int(product.stock)
                    the_stock += new_stock
                    p1.stock = the_stock
                    with open('Products.pkl', 'wb') as f:
                        pickle.dump(p1, f)
                    print("Stock added")
                elif the_id == product_to_edit:
                    print("Product found")
                    new_stock = int(
                        input("Enter how much stock you want to add: "))
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
        ShopMethods.view_products()
        inp = open('Products.pkl', 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                print("end of products\n")
                cont = 0
        product_to_edit = int(
            input("Enter the id of the product you want to reduce stock: "))
        first_object = objects[0]
        for product in objects:
            the_id = int(product.id)
            p1 = Product(product.id, product.name, product.price,
                         product.stock, product.brand)
            try:
                if the_id == first_object.id:
                    print("Product found")
                    new_stock = int(
                        input("Enter how much stock you reduce to reduce: "))
                    the_stock = int(product.stock)
                    the_stock -= new_stock
                    p1.stock = the_stock
                    with open('Products.pkl', 'wb') as f:
                        pickle.dump(p1, f)
                    print("Stock reduced")
                elif the_id == product_to_edit:
                    print("Product found")
                    new_stock = int(
                        input("Enter how much stock you want to reduce: "))
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
        ShopMethods.view_products()
        inp = open('Products.pkl', 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                print("end of products\n")
                cont = 0
        product_to_edit = int(
            input("Enter the id of the product you want to edit: "))
        first_object = objects[0]
        for product in objects:
            the_id = int(product.id)
            p1 = Product(product.id, product.name, product.price,
                         product.stock, product.brand)
            try:
                if the_id == first_object.id:
                    p1 = Product(Product.set_id(BasicMethods.askInteger("ID")), Product.set_name(BasicMethods.askString("Name")), Product.set_price(BasicMethods.askInteger("Price")), Product.set_stock(BasicMethods.askString("Stock")), Product.set_brand(BasicMethods.askString("Brand")))
                    with open('Products.pkl', 'wb') as f:
                        pickle.dump(p1, f)
                    print("Product edited")
                elif the_id == product_to_edit:
                    p1 = Product(Product.set_id(BasicMethods.askInteger("ID")), Product.set_name(BasicMethods.askString("Name")), Product.set_price(BasicMethods.askInteger("Price")), Product.set_stock(BasicMethods.askString("Stock")), Product.set_brand(BasicMethods.askString("Brand")))
                    with open('Products.pkl', 'ab') as f:
                        pickle.dump(p1, f)
                    print("Product edited")
                else:
                    with open('Products.pkl', 'ab') as f:
                        pickle.dump(p1, f)
            except EOFError:
                print("No product found with that id")

    def remove_product():
        ShopMethods.view_products()
        inp = open('Products.pkl', 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                print("end of products\n")
                cont = 0
        product_to_delete = BasicMethods.askString("ID for the product you want to delete ")
        first_object = objects[0]
        contt = 0
        is_the_first = 0
        for product in objects:
            the_id = int(product.id)
            p1 = Product(product.id, product.name, product.price,product.stock, product.brand)
            try:
                if product_to_delete == first_object.id and is_the_first == 1:
                    with open('Products.pkl', 'wb') as f:
                        pickle.dump(p1, f)
                elif product_to_delete != first_object.id and contt == 0:
                    with open('Products.pkl', 'wb') as f:
                        pickle.dump(p1, f)
                    contt = 1
                    is_the_first = 1
                elif the_id == product_to_delete and contt == 0:
                    contt = 1
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
        p1 = Product(Product.set_id(BasicMethods.askInteger("ID")), Product.set_name(BasicMethods.askString("Name")), Product.set_price(BasicMethods.askInteger("Price")), Product.set_stock(BasicMethods.askString("Stock")), Product.set_brand(BasicMethods.askString("Brand")))
        with open('Products.pkl', 'ab') as f:
            pickle.dump(p1, f)
        print("Product added")

    def exit_program():
        print("Thank you for using the program")

   
