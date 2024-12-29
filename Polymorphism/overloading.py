class Calc:
 def add(self, *args):
   return sum(args)
 
calc = Calc()
print(calc.add(10,5)) 
print(calc.add(10,5,5))


 