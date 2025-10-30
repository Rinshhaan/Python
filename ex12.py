# Q) The areas of the various continents of the world (in millions of
# square miles) are as follows: 11.7 for Africa; 10.4 for Asia; 1.9 for
# Europe; 9.4 for North America; 3.3 Oceania; 6.9 South America;
# 7.9 Soviet Union. Draw a bar chart representing the given data.

import matplotlib.pyplot as plt

areas = ['africa', 'asia', 'europe', 'north-america', 'oceania', 'south-america', 'soviet-union']
miles = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]

plt.bar(areas, miles, color='red', edgecolor='black', label='Areas of continents')
plt.title('Areas of Continents')
plt.xlabel('Continents')
plt.ylabel('Area (in millions of square miles)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.xticks(rotation=45)
plt.show()