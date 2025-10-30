# ALGORITHM
# STEP 1:Start.
# STEP 2:Take three numbers as input from the user.
# STEP 3:Use conditional statements to compare the numbers and find the largest. STEP 4:Print the largest number.
# STEP 5:Stop.

def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
print("Enter three numbers: ")
num1 = input("Enter a num1: ")
num2 = input("Enter a num2: ")
num3 = input("Enter a num3: ")

largest_number = largest(num1,num2,num3)
print("The largest number is:", largest_number)
