import matplotlib.pyplot as plt
import numpy as np

data=np.random.rand(10,5)*100

plt.boxplot(data)

plt.title("box plot with whiskers")
plt.show()