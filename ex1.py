import numpy as np
import matplotlib.pyplot as plt
# Q) write a python program to check prime numbers or not
def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
    return True


n = int(input("Enter a number: "))
if prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")


# Q) Histogram
boundaries = [30000,35000,40000,45000,50000]

no_of_people = np.array([10,5,20,5])

data = []
for i in range(len(no_of_people)):
    data.extend([ (boundaries[i]+boundaries[i+1])/2 ]*no_of_people[i])

plt.hist(data,bins=boundaries,color='blue',edgecolor='black')
plt.title("Histogram")
plt.xlabel("income range")
plt.ylabel("no of people")
plt.grid(axis='y',linestyle=':',alpha=0.6)
plt.show()