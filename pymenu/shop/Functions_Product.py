import pickle
import os
from Product import Product
import BasicMethods

def Shop_menu():
        print("1. Add product")
        print("2. View all products")
        print("3. Change stock")
        print("4. Edit product")
        print("5. Remove product")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Functions_Product.add_product()
            Functions_Product.Shop_menu()
        elif choice == "2":
            Functions_Product.view_products()
            Functions_Product.Shop_menu()
        elif choice == "3":
            Functions_Product.stock_menu()
            Functions_Product.Shop_menu()
        elif choice == "4":
            Functions_Product.edit_product()
            Functions_Product.Shop_menu()
        elif choice == "5":
            Functions_Product.remove_product()
            Functions_Product.Shop_menu()
        elif choice == "0":
            Functions_Product.exit_program()
        else:
            print("Invalid choice")
            Functions_Product.Shop_menu()


class Functions_Product:

    def saveProduct(self,obj, filename):
        with open(filename, 'ab') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    def add_product(self):
        p1 = Product()
        p1.setId()
        p1.setName()
        p1.setBrand()
        p1.setPrice()
        p1.setStock()
        p1.print()
        function_Product = Functions_Product()
        function_Product.saveProduct(p1, 'Products.pkl')

    def stock_menu():
        print("1. Add stock to a product")
        print("2. Remove stock from a product")
        print("0. Exit")
        choice = BasicMethods.askString("your choice")
        if choice == "1":
            Functions_Product.add_stock_to_product()
            Functions_Product.stock_menu()
        elif choice == "2":
            Functions_Product.remove_stock_from_product()
            Functions_Product.stock_menu()
        elif choice == "0":
            Functions_Product.exit_program()
        else:
            print("Invalid choice")
            Functions_Product.stock_menu()

    def add_stock_to_product():
        if os.path.exists('Products.pkl'):
            Functions_Product.view_products()
            product_to_edit = input(BasicMethods.askInteger("the id of the product you want to edit: "))
            f = open('Products.pkl', 'rb')
            products = []
            cont = 1
            while cont == 1:
                try:
                    products.append(pickle.load(f))
                except EOFError:
                    cont = 0
            f.close()
            if os.path.exists("Products.pkl"):
                os.remove("Products.pkl")
            for cl in products:
                    if cl.id != product_to_edit:
                        Functions_Product.saveProduct(cl, 'Products.pkl')
                    elif product_to_edit == cl.id:
                        p1 = Product
                        p1.id = cl.id
                        p1.name = cl.name
                        p1.price = cl.price
                        p1.stock = int(input("Enter the amount of stock you want to add: ")) + int(cl.stock)
                        p1.brand = cl.brand
                        Functions_Product.saveProduct(p1, 'Products.pkl')
                        print("product edited")
                    else:    
                        print("product not found")
   
    def remove_stock_from_product():
        print("Removing stock from a product")
        if os.path.exists('Products.pkl'):
            function_Product = Functions_Product()
            function_Product.viewProducts()
            productId = input("Enter the id of the product: ")
            inp = open('Products.pkl', 'rb')
            objects = []
            cont = 1
            while cont == 1:
                try:
                    objects.append(pickle.load(inp))
                except EOFError:
                    cont = 0
            inp.close()
            if os.path.exists('Products.pkl'):
                os.remove('Products.pkl')
            for cl in objects:
                if int(cl.id) != int(productId):
                    function_Product.saveProduct(cl, 'Products.pkl')
                elif int(cl.id) == int(productId):
                    p1 = Product
                    p1.id = cl.id
                    p1.name = cl.name
                    p1.price = cl.price
                    p1.stock = int(cl.stock) - int(input("Enter the amount of stock you want to add: ")) 
                    p1.brand = cl.brand
                    Functions_Product.saveProduct(p1, 'Products.pkl')
                else:
                    print("There isn't any product with the same id ")
        else:
            print("There aren't any products")

    def remove_product(self):
        if os.path.exists('Products.pkl'):
            function_Product = Functions_Product()
            function_Product.viewProducts()
            productId = input("Enter the id of the product: ")
            inp = open('Products.pkl', 'rb')
            objects = []
            cont = 1
            while cont == 1:
                try:
                    objects.append(pickle.load(inp))
                except EOFError:
                    print("end of products\n")
                    cont = 0
            inp.close()
            if os.path.exists('Products.pkl'):
                os.remove('Products.pkl')
            for cl in objects:
                if int(cl.id) != int(productId):
                    function_Product.saveProduct(cl, 'Products.pkl')
        else:
            print("There aren't any products")

    def view_products(self):
        if os.path.exists('Products.pkl'):

            inp = open('Products.pkl', 'rb')
            objects = []
            cont = 1
            while cont == 1:
                try:
                    objects.append(pickle.load(inp))
                except EOFError:
                    print("end of products\n")
                    cont = 0
            for cl in objects:
                cl.print()
        else:
            print("There aren't any products")


    def edit_product(self):
        print("Modifying products")
        if os.path.exists('Products.pkl'):
            function_Product = Functions_Product()
            function_Product.viewProducts()
            productId = input("Enter the id of the product: ")
            inp = open('Products.pkl', 'rb')
            objects = []
            cont = 1
            while cont == 1:
                try:
                    objects.append(pickle.load(inp))
                except EOFError:
                    cont = 0
            inp.close()
            if os.path.exists('Products.pkl'):
                os.remove('Products.pkl')
            for cl in objects:
                if int(cl.id) != int(productId):
                    function_Product.saveProduct(cl, 'Products.pkl')
                elif int(cl.id) == int(productId):
                    p1 = Product()
                    p1.setIdWP(productId)
                    p1.setName()
                    p1.setStock()
                    p1.setPrice()
                    p1.setBrand()
                    function_Product.saveProduct(p1, 'Products.pkl')
                else:
                    print("There isn't any product with the same id ")
        else:
            print("There aren't any products")

    def exit_program(self):
        print("Exiting program")
        exit()

Shop_menu()