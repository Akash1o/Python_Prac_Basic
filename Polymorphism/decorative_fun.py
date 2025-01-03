def decorative_fucntion(func):
    def wrapper():
        print("This is before the function call")
        func()
        print("This is after the function call")
    return wrapper

@decorative_fucntion
def say_namaste():
    print("Namaste")

say_namaste()




 '''
 decorative function helps in
  putting addtional fucntionality before and after
of the function call . It wraps the function inside it.

 it can also be assigned by this way :
 say_namaste = decorative_fucntion(say_namaste)
say_namaste()


 '''

