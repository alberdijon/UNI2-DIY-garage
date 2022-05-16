class Product:
    def __init__(self, id, name, price, stock, brand):
        self.id = int(id)
        self.name = str(name)
        self.price = int(price)
        self.stock = int(stock)
        self.brand = str(brand)

    def get_id(self):
        return self.id
    def set_id(self,a):
        self.id = a
    def get_name(self):
        return self.name
    def set_name(self,a):
        self.name = a
    def get_price(self):
        return self.price
    def set_price(self,a):
        self.price=a
    def get_stock(self):
        return self.stock
    def set_stock(self,a):
        self.stock=a
    def get_brand(self):
        return self.brand
    def set_brand(self,a):
        self.brand=a