from matplotlib import pyplot as plt
import numpy as np

x=np.arange(-9, 10)
y=x**2

plt.plot(x,y, linestyle=":", marker="*")
plt.show()