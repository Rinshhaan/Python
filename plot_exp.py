import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0,color='black') # creates a line at (0)
plt.axvline(0,color='black') # creates a vertical line at 0

plt.plot(3,2,color='red',marker='*')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.grid(True)
plt.show()

"""
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]
colors = ['red', 'yellow', 'pink', 'brown']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# plt.title("Fruit Distribution")
# plt.show()

x = np.random.rand(50)
y = np.random.rand(50)

# plt.scatter(x, y, color='red', marker='*')
"""