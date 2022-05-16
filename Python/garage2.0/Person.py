class Person:

    def __init__(self,id,first_name,last_name,email,phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_id(self):
        return self.id
    def set_id(self,a):
        self.id = a
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
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self,a):
        self.phone_number = a