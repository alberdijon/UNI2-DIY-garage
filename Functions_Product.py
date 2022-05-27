import pickle
import os
from Product import Product
from BasicMethods import BasicMethods

class Functions_Product:

    def saveProduct(self,obj, filename):
        with open(filename, 'ab') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


    def Shop_menu(self):
        print("\n")
        print("Shop Menu -->")
        print("----------------")
        print("1. Add product")
        print("2. View all products")
        print("3. Change stock")
        print("4. Edit product")
        print("5. Remove product")
        print("0. Exit")
        print("\n")
        product_choice = input("Enter your choice: ")
        print("\n")
        return  product_choice


    def add_product(self):
        p1 = Product()
        p1.setId()
        p1.setName()
        p1.setBrand()
        p1.setPrice()
        p1.setStock()
        p1.print()
        function_Product = Functions_Product()
        function_Product.saveProduct(self, p1, 'Products.pkl')

    def stock_menu(self):
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
            print("Exiting")
        else:
            print("Invalid choice")
            Functions_Product.stock_menu()

    def add_stock_to_product(self):
        print("Adding stock from a product")
        if os.path.exists('Products.pkl'):
            functions_product = Functions_Product()
            functions_product.view_products()
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
            for c1 in products:             
                    if int(c1.id) != product_to_edit:
                        functions_product.saveProduct(c1, 'Products.pkl')
                    elif product_to_edit == int(c1.id):
                        actual_stock = int(c1.stock)
                        c1.stock = int(input("Enter the amount of stock you want to add: ")) + actual_stock
                        functions_product.saveProduct(c1, 'Products.pkl')
                        print("product edited")
                    else:    
                        print("product not found")
   
    def remove_stock_from_product(self):
        print("Remving stock from a product")
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
            for c1 in products:
                    c1 = Product()               
                    if c1.id != product_to_edit:
                        Functions_Product.saveProduct(c1, 'Products.pkl')
                    elif product_to_edit == c1.id:
                        p1 = Product
                        p1.id = c1.id
                        p1.name = c1.name
                        p1.price = c1.price
                        p1.stock = int(c1.stock) - int(input("Enter the amount of stock you want to add: "))
                        p1.brand = c1.brand
                        Functions_Product.saveProduct(p1, 'Products.pkl')
                        print("product edited")
                    else:    
                        print("product not found")

    def remove_product(self):
        if os.path.exists('Products.pkl'):
            function_Product = Functions_Product()
            function_Product.view_products()
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
            for c1 in objects:
                if int(c1.id) != int(productId):
                    function_Product.saveProduct(c1, 'Products.pkl')
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
                    cont = 0
            for c1 in objects:
                c1.print()
        else:
            print("There aren't any products")


    def edit_product(self):
        print("Modifying products")
        if os.path.exists('Products.pkl'):
            function_Product = Functions_Product()
            function_Product.view_products()
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
            for c1 in objects:
                c1 = Product()
                if int(c1.id) != int(productId):
                    function_Product.saveProduct(c1, 'Products.pkl')
                elif int(c1.id) == int(productId):
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


c1 = Product("1", "oil", "repsol", "10", "58")
with open('Products.pkl', 'wb') as f:
    pickle.dump(c1, f)