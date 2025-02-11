import numpy as np
import pandas as pd

#4x4 matrix with random numbers.
df =pd.DataFrame(np.random.randint(10,100,(4,4)))

#getting max top 4 
max_four = np.sort(df.values.flatten())[-4:]
#df.values changes into numpy array 
#convert 2d array into 1d

two_matrix_form =pd.DataFrame(max_four.reshape(2,2))
#converts 1d array to 2x2 matrix


print(df)
print(max_four)
print(two_matrix_form)

