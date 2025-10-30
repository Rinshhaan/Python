import matplotlib.pyplot as plt
import numpy as np

#Height of students (cm): 135–140  140–145  145–150  150–155
#Number of students:         4       12       16       8

# Class intervals (bins)
heights = [135, 140, 145, 150,155]  # class boundaries
# heights = np.array([135, 140, 145, 150])  # class boundaries
#heights2 = np.array([140, 145, 150, 155])
#mid = (heights+heights2)/2
#print(mid)
# Frequencies (number of students)
students = [4, 12, 16, 8]

# Plot the histogram using bar()
plt.bar(
    x=[137.5,142.5,147.5,152.5],  # midpoints of each class
    height = students,
    width=5,                          # width of each bar (difference between intervals)
    color='skyblue',
    edgecolor='black'
)

# Add labels and title
plt.xlabel('Height of Students (cm)')
plt.ylabel('Number of Students')
plt.title('Histogram of Student Heights')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Show the plot
plt.show()
