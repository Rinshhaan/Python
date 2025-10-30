# Q) Develop a program to find the largest of three numbers and check if the largest number is prime.

def largest(a,b,c):
    if a>b and a> c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True  

n1 = int(input("Enter number"))
n2 = int(input("Enter number"))
n3 = int(input("Enter number"))

largest_num = largest(n1,n2,n3)

if prime(largest_num):
    print(f"{largest_num} is Prime number")
else:
    print(f"{largest_num} is not prime")
