# ALGORITHM
# STEP 1: Start.
# STEP 2: Input numbers and create a tuple.
# STEP 3: Use tuple comprehensions to separate even and odd numbers. 
# STEP 4: Print the even and odd tuples.
# STEP 5: Stop.

numbers = tuple(map(int,input("Enter the numbers seperated by spaces: ").split()))
print(numbers)

odd_numbers = tuple(num for num in numbers if num % 2 !=0)
even_numbers = tuple(num for num in numbers if num % 2 ==0)

print(f"Odd numbers: {odd_numbers} and even numbers: {even_numbers}")

