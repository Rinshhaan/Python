import scipy.stats as stats

# Given data
n = 16
Sample_mean = 22
Sample_sd = 3
Pop_mean = 20
Alpha = 0.05

# t statistic
T_stat = (Sample_mean - Pop_mean) / (Sample_sd / (n ** 0.5))

# Degrees of freedom
Df = n-1

#p-value (two-tailed test since we are checking difference from pop_mean)
P_value = 2 * (1 - stats.t.cdf(abs(T_stat), Df))

print("Q21: Truck MPG Test")
print("t-statistic:", round(T_stat, 4))
print("p-value:", round(P_value, 4))

if P_value < Alpha:
    print("Reject the null hypothesis (mean MPG differs significantly from 20).")
else:
    print ("Fail to reject the null hypothesis (no significant difference).")
