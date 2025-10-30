# ALGORITHM
# STEP 1: Start
# STEP 2: Import matplotib.pyplot library to plot histogram
# STEP 3: Define bins (height based) and generate data based on given frequencies
# STEP 4: Create a histogram using generated data and defined bins 
# STEP 5: Customize the histogram with title and label
# STEP 6: Display the histogram
# STEP 7: Stop



import matplotlib.pyplot as plt

# Class intervals and frequencies
intervals = [135, 140, 145, 150, 155] # boundaries = bins
frequencies = [4, 12, 16, 8]

# eg: ((135+140)/2)*4 
# To use plt.hist, we need to expand the data into actual values
# Example: 4 students between 135–140 means we can represent it by repeating that value

data = []
for i in range(len(frequencies)): # 4
    data.extend([ (intervals[i] + intervals[i+1]) / 2 ] * frequencies[i]) #extend must
print(data) 

# Now plot histogram
plt.hist(data, bins=intervals, color='lightgreen', edgecolor='black')

plt.xlabel("Height of Students (cm)")
plt.ylabel("Number of Students")
plt.title("Histogram using plt.hist()")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
