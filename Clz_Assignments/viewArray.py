import numpy as np

arr = np.array([1,2,3,4,5,6])
view = arr.view()
view[1] = 12

print("before view",arr)
print("after view",view)

'''
view changes on orginal array also 
but copy doesnt 
'''


copy =arr.copy()
copy[1]=0
print("the real ",arr)
print("the copy filed",copy)