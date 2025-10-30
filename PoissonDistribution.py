# ALGORITHM
# STEP 1: Start
# STEP 2: Input lamda and k
# STEP 3:
# STEP 4:
# STEP 5:
# STEP 6:
# STEP 7:


# If the random variable follow a Poisson distribution with mean 3.4 find P(X=6).

import math 

# Given parameter 
Lambda = 3.4 # Mean of the Poisson distribution 
k = 6 # number of event 

# Calculate Poisson probability P(X = k) 
prob_6 = (Lambda** k)*math.exp(-Lambda)/ math.factorial(k) 
# Print the re ult 
print(f"P(X = {k}) for Poisson distribution with mean {Lambda}: {prob_6:.4f}")