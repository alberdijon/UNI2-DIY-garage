
class User:
    def __init__(self, first_name, last_name, email, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number


    def get_first_name(self):
        return self.first_name
    def set_first_name(self, a):
        self.first_name = a
    def get_last_name(self):
        return self.last_name
    def set_last_name(self, a):
        self.last_name = a
    def get_email(self):
        return self.email
    def set_email(self, a):
        self.email = a
    def get_password(self):
        return self.password
    def set_password(self,a):
        self.password = a 
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self,a):
        self.phone_number = a

