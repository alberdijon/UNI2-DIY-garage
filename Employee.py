from BasicMethods import BasicMethods
from Person import Person

class Employee(Person):
    def __init__(self, id, name, last_name, email, phone_number, job, salary):
        super().__init__(id, name, last_name, email, phone_number)

        self.job = ""
        self.salary = 0

    def set_job(self, job):
        self.job = BasicMethods.askString("the job: ")
    
    def get_job(self):
        return self.job
    
    def set_salary(self, salary):
        self.salary = BasicMethods.askInteger("the salary: ")
    
    def get_salary(self):
        return self.salary
    
    
    def print(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Last name: ", self.last_name)
        print("Email: ", self.email)
        print("Phone number: ", self.phone_number)
        print("Job: ", self.job)
        print("Salary: ", self.salary)
