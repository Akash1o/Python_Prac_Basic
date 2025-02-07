import numpy as np

# Checking odd or even
arrays_nums = np.array([1, 4, 5, 6, 7, 2])

# Using np.where to label even and odd numbers
result = np.where(arrays_nums % 2 == 0, "Even", "Odd")

print("Numbers:", arrays_nums)
print("Labels :", result)


age =np.array([12,13,45,18,15,14,12,11])
results=np.where(age < 18," minor", " adult")
print(results)