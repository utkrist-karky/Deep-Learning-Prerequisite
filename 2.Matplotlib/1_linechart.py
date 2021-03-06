import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,1000)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = sin(x)')
plt.show()