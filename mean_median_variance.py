# ALGORITHM 
# STEP I: Start. 
# STEP 2: Define states and their populations in a list or dictionary. 
# STEP 3: Calculate mean, median, and variance using NumPy. 
# STEP 4: Display the results. 
# STEP 5: Stop.

import numpy as np 
# Data 
states = ["Alabama" , "Alaska" , "Arizona" , "Arkansas" , "California" , "Colorado" , "Connecticut" , "Delaware"] 
populations = [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934]

# Compute statistics 
mean_population = np.mean(populations) # (all +)/len(population)
median_population = np.median(populations) # if n = odd, median = middlevalue elif n = even , median = middle two values + then / 2
variance_populaton = np.var(populations) # sigmasquare = ((population[i]-mean)^2)/n)

# Print the results

print(f"mean Population: {mean_population}")
print(f"Median Population: {median_population}") 
print(f"Variance of Population: {variance_populaton}")