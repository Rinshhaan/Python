import matplotlib.pyplot as plt

plt.axhline(0,color='black') # creates a line at (0)
plt.axvline(0,color='black') # creates a vertical line at 0

plt.plot(3,2,color='red',marker='*')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.grid(True)
plt.show()