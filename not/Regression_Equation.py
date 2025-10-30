import numpy as np
from scipy import stats

job_satisfaction = np.array([34,23,19,43,56,47,32,16,55,25])
Systolic_BP = np.array([124,128,157,133,116,125,147,167,110,158])

# perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(job_satisfaction, Systolic_BP)

# display the regression equation
print(f"Regression Equation: y = {intercept:.2f} + {slope:.2f}x")

# prediction for job satisfaction = 15
x_predict = 15
y_predict = intercept + slope * x_predict

print(f"Predicted Systolic BP when Job Satisfaction is {x_predict}: {y_predict:.2f}")

# residuals
residuals = Systolic_BP - (slope * job_satisfaction + intercept)

# standard error of the estimate(SEE)
SEE = np.sqrt(np.sum(residuals**2) / (len(job_satisfaction) - 2))
print(f"Standard Error of the Estimate (SEE): {SEE:.2f}")

# correlation coefficient R and R squared
print(f"Correlation Coefficient R: {r_value:.3f}")
print(f"Coefficient of Determination R^2: {r_value**2:.3f}")
