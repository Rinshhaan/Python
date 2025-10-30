# ALGORITHM
# STEP 1: Start. 
# STEP 2: Define the class intervals and their frequencies. 
# STEP 3: Calculate the mean, variance, and standard deviation using the formula. 
# STEP 4: Compute the coefficient of variation. 
# STEP 5: Display the results. 
# STEP 6: Stop.

import numpy as np 
# Data 
class_intervals = ["0-1O" , "10-20" , "20-30" , "30-40" , "40-50" , "50-60" , "60-70" , "70-80"]
frequencies = [5, 10, 20, 40, 30, 20, 10, 5]

# Calculate midpoints 
midpoints= [5, 15, 25, 35, 45, 55, 65, 75] 

# Weighted mean 
mean = np.average(midpoints, weights=frequencies) 
print(mean)

# Variance and standard deviation 
squared_deviation = [(x - mean)**2 for x in midpoints] 
print(squared_deviation)
variance = np.average(squared_deviation, weights=frequencies) 
std_dev = np.sqrt(variance) 

# Coefficient of Variation 
cv = (std_dev/mean)* 100 
# Results 
print(f"Mean: {mean}") 

print(f"Standard Deviation: {std_dev}") 
print(f"Coefficient of Variation (C.V.): {cv:.2f}%")