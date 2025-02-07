import numpy as np
arr= np.array([1,2,3,4,5,6,7,8,9])
print(f"Before the reshape is : {arr}")
reshaped = arr.reshape(3,3) #convert into 3*3 matrix
print(f"after reshape: {reshaped}")