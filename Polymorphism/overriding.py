class Father:
    def eat(self):
        print("Father eats")

class Son (Father):
    def eat(self):
        print("Son eats")

class Daughter (Father):
    def eat(self):
        print("Daughter eats")      

 #instance creation 
Dad = Father()
Son = Son()
Daughter = Daughter()

#calling the method which are overridden
Dad.eat()
Son.eat()
Daughter.eat()
       