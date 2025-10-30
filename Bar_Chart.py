# Q) The areas of the various continents of the world (in millions of square miles) are as follows: 11. 7 for Africa; I 0.4 for Asia; 1.9 for Europe; 9.4 for North America; 3.3 Oceania; 6.9 South America; 7.9 Soviet Union. Draw a bar chart representing the given data. 
# ALGORITHM 
# STEP l: Start. 
# STEP 2: Define the continents and their respective areas as lists. 
# STEP 3: Use Matplotlib to create a bar chart. 
# STEP 4: Label the axes and title the graph. 
# STEP 5: Display the bar chart. 
# STEP 6: Stop. 

import matplotlib.pyplot as plt 
# Data 
continents = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America",  "Soviet Union"] 
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9] 
# Plot the bar chart 
# plt.bar(list1,lits2,styles)
plt.bar(continents, areas, color='RED',label='bargraph') 
plt.title("Areas of Continents (in millions of square miles)") 
plt.xlabel("Continents") 
plt.ylabel("Area") 
plt.xticks(rotation=45) 
plt.legend()
plt.grid(axis='y',linestyle='--',alpha = 1.0)  # axis y means horizontal lines and alpha is for transparency
plt.show()