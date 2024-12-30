class Cars:
    def __init__(self,name,model):
        self.name=name #public attribute
        self._model = model #protected attribute
        self.__price = 1000000 
        #private attribute show it is not in constructor
    def display(self):
        print(f"Name: {self.name} ")
        print(f"Model: {self._model}")
        print(f"Price: {self.__price}")
        

        def get_price(self):
            return self.__price
        #a public method can access  prrivate attribute

        #object creation

car1 =Cars("BMW",2024)

    #accessing publicand protected attributes
print(car1.name) #public atrribute works 

print(car1._model) #works but protected.

# print(car1.__price) #error because it is private
