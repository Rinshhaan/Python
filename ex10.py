# Q) In a cafe, the customer arrives at a mean rate of 2 per min. Find the
# probability of arrival of 5 customers in 1 minute using the Poisson
# distribution formula.

import math

lam = 2
k = 5


prob = ((lam**k)*math.exp(-lam))/math.factorial(k)

print(f"Probability of exactly {k} customers in 1 minute: {prob:.4f}")