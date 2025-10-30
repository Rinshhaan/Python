import numpy as np
from scipy.stats import chi2_contingency
# Observed frequency table
# Rows: Female, Male
# Columns: High School, Bachelors, Master, Ph.D

observed = np.array([
[60, 54, 46, 41], # Female 
[40, 44, 53, 57]
])#Male               
      
# Perform Chi-Square test
chi2, p, dof, expected = chi2_contingency(observed)

# Display results
print ("Observed Frequencies: \n", observed)
print("\nExpected Frequencies: In", np.round(expected, 2))
print("Chi-Square Statistic:", round(chi2, 2))
print("Degrees of Freedom:", dof)
print("P-value:", round(p, 4))

# Significance level
alpha = 0.05
if p < alpha:
    print("InConclusion: Reject the null hypothesis. Gender and education level are dependent.")
else:
    print("InConclusion: Fail to reject the null hypothesis. Gender and education level are independent.")