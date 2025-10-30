# Q) if the probability of choosing incorrect answer in an examination is 0.01,
# determine the chance out of 500 students more than 1 will choose incorrect answers
import math

n=500
k=1
p=0.01

#! here n is larger than p so we use poisson distribution

# to finde mean(lamda)
lamda_ = n * p  # 500 x 0.01

# p(X>1)
# since p(X > 1) = we use 1 - p[X = 0] + p[X = 1]  

prob_0 = ((lamda_**0)*math.exp(-lamda_))/math.factorial(0) 
prob_1 = ((lamda_**1)*math.exp(-lamda_))/math.factorial(1) 

prob = 1-(prob_0 + prob_1)

print(prob)