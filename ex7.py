# Q) calculate the probability of getting exactly five heads when a coin is tossed

import math


n = 10 # times
p = 0.5
k = 5 # p(x=5


prob_5 = math.comb(n,k)*(p**k)*((1-p)**(n-k))

print(prob_5)