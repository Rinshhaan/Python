# Q) write a python program to draw following bar graph

import matplotlib.pyplot as plt

x = ["One","two","three","four","five"]
y = [10,25,35,40,5]

colors = ['red','green','red','green','red']

plt.bar(x,y,color=colors,edgecolor='blue')
plt.xlabel('numbers')
plt.ylabel('values')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.3)
plt.show()