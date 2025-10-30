def largestofThree(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    

print("Enter three numbers: ");
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter second number: "))
largest = largestofThree(a,b,c)
print(f"The largest is {largest}")


#! algorithm
# 1. start the program
# 2. prompt the user to input three numbers
# 3. compare first number with second and third
# 4. if first number is greater than other numbers, return first number
# 5. else compare second and third number
# 6. display the largest number 
# 7. end the program