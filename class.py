class Employee:
    def __init__(self, name, age, address):
#__init__ constructor method for intialize objects attributs.
#self instance of the class.

     self.name = name
     self.age = age
     self.address = address

    def display_show(self):
         print(f"Name: {self.name} Age: {self.age} Address: {self.address}")

Emp1 = Employee("Suresh", 22,"Kathmandu")
Emp1.display_show()
