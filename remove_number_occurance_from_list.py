# ALGORITHM
# STEP 1: Start.
# STEP 2: Input a list of numbers. 
# STEP 3: Input the number to remove.
# STEP 4: Use a 'list comprehension' to 'filter out all occurrences of the number'. 
# STEP 5: Print the updated list.
# STEP 6: Stop.


numbers = list(map(int,input("Enter numbers seperated by commas: ").split(",")))
print(numbers)
number_remove = int(input("enter the number to remove: "))

if number_remove not in numbers:
    print("The number to be removed is not found in the list.")
    exit()

updated_list = [num for num in numbers if num != number_remove] # list comprehension to filter out all occurrences of number_remove
print(updated_list)