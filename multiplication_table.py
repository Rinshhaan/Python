# ALGORITHM
# STEP 1: Start.
# STEP 2:Input a number n from the user.
# STEP 3:Use a loop to multiply n with numbers from 1 to 10. 
# STEP 4:Print the results in tabular format.
# STEP 5:Stop.

n = int(input("Enter the number to generate multiplication table: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    