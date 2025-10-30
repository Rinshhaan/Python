import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(-10, 10, 200)
y1 = x**2        # y = x²
y2 = 2*x         # y = 2x
y3 = x**3        # y = x³


plt.plot(x, y1, label="y = x²", color='blue', linestyle='-')
plt.plot(x, y2, label="y = 2x", color='green', linestyle='--')
plt.plot(x, y3, label="y = x³", color='red', linestyle=':')

plt.title("Multiple Functions: y = x², y = 2x, y = x³")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.show()
