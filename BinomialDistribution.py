# If X is binomially distributed with 6 trials and a probability of success equal to 0.25 at 
# each attempt, what is the probability of: 
# a)	exactly 4 successes
# b)	at least one success

# exactly 4 => p(X=4)
# atleast 1 => p(X >= 1)
# atmost => p(X <= n)
# more than => >
# less tha => <

import math
# Parameters

n = 6 # Number of trials 
p = 0.25 # Probability of success

# a) Probability of exactly 4 successes (P(X = 4))
k1 = 4  # x value
prob_4_successes = math.comb(n,k1)*(p**k1)*((1 - p)**(n - k1))


# b) Probability of at least 1 success (P(X >= 1))= 1 - P(X = 0)
k2 = 0
prob_0_successes = math.comb(n, k2)*(p**k2)*((1 - p)**(n - k2)) 
# Calculate probability for at least I success 
prob_at_least_l_success = 1 - prob_0_successes 

print(f"Probability of exactly 4 successes: {prob_4_successes:.4f}") 
print(f"Probability of atleast I success: {prob_at_least_l_success:.4f}")