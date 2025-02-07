import numpy as np

random_values =np.random.rand(3,3)
#generate 3*3 random matrix values

print(random_values)

#random int numbers.
ints =np.random.randint(10,50)
int =np.random.randint(10,50,size=(2,2))
print(int,ints)


#simulating dice rools

dice=np.random.randint(1,7,size=8)
print("Dice rolls:", dice)
