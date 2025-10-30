# Q) write a python program to input a point and find the quadrant and also plot

import matplotlib.pyplot as plt

# Input coordinates
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

# Plot setup
plt.axhline(0, color='black')   # X-axis zero means at 0th value a line 
plt.axvline(0, color='black')   # Y-axis
plt.grid(True, linestyle='--', alpha=0.6)

# Plot the point
plt.scatter(x, y, color='red', s=100, label=f"Point ({x}, {y})")  # s = size of point

# Set axis limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Determine and label the quadrant
if x > 0 and y > 0:
    plt.title("Quadrant I")
elif x < 0 and y > 0:
    plt.title("Quadrant II")
elif x < 0 and y < 0:
    plt.title("Quadrant III")
elif x > 0 and y < 0:
    plt.title("Quadrant IV")
elif x == 0 and y == 0:
    plt.title("Origin")
elif x == 0:
    plt.title("On Y-axis")
else:
    plt.title("On X-axis")

plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
