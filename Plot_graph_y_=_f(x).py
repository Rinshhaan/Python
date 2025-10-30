# ALGORITHM 
# STEP I : Start. 
# STEP 2: Define a function f(x). 
# STEP 3: Generate values of x using NumPy or a range. 
# STEP 4: Calculate y=f(x) for each x. 
# STEP 5: Use Matplotlib to plot the graph. 
# STEP 6: Stop. 

import matplotlib.pyplot as plt 
import numpy as np 
# Define the function f(x) 
def f(x):
    return x**2  # Example function: f(x) = x²

# Generate x values 
x = np.linspace(-10, 10, 100) #! This makes 100 evenly spaced numbers from -10 to 10.
print(x)
y = f(x)
#y = x**2       # f(x) = x²
#print(y)
# Plot the graph 
plt.plot(x, y, label="y = x^2",marker='o') #! label is used to show in legend and plot used to draw graph
plt.title("Graph of y = x^2") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.grid(True) #! to show grid lines
plt.legend() #! used to show label box
plt.show()