#all array slicing operations.

import numpy as np

#creating an array.
arr=np.array([0,1,2,3,4,5,6,7])

print(arr)

#basic slicing 
sliced=arr[3:5]
#arr[start:end] start inclusive and end is exclusive

print(sliced)


#omitting start and end 
front=arr[:4] #from the beginning to index 4
back=arr[4:]   #from index 4 to the end
print(front )
print(back)