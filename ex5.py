# write a python program to plot the curve f(x) = 2x^2-1 for values of x between -5 and +5

import matplotlib.pyplot as plt
import numpy as np

"""
def f(x):
    return ((2*x)**2)-1 """

x = np.linspace(-5,5,100)
#y = f(x)
y=(2*x)**2-1

plt.plot(x,y,color='red',label='2x^2-1')
plt.title('f(x) = 2x^2-1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()