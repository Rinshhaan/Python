# ALGORITHM
# STEP 1: Start.
# STEP 2: Read numbers from a file.
# STEP 3: Define a function to check if a number is prime. 
# STEP 4: Iterate through the numbers and print primes.
# STEP 5: Stop.


# Function to check if a number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to read numbers from the file and print primes 
def find_primes_from_file(file_name):
    try:
        with open(file_name, 'r') as file: # used with to automatically close the file after usage and assign file object to variable 'file'

            lines = file.readlines() # ['ha saaa a 333 44\n', '11\n', '12\n', '3\n', '000\n', ' haz']
            print(f'{lines}')

        for line in lines: 
            print(f'{line}') # ha saaa a 333 44
            
            words = line.split() 
            print(f'{words}') # ['ha', 'saaa', 'a', '333', '44']

            for word in words:
                print(f'{word}')
                
                try:
                    num = int(word)
                    if is_prime(num):
                        print(f"{num} is a prime number.")
                    else:
                        print(f"{num} is not a prime number.")
                except ValueError:
                    # skip words that are not numbers
                    pass

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


# Main program
file_name = input("Enter the name of the file containing numbers: ")
find_primes_from_file(file_name)


#! note: AttributeError: 'list' object has no attribute 'split'


'''

def find_primes_from_file(file_name):
try:
with open(file_name, 'r') as file: 
    numbers = file.readlines()
# Convert numbers to integers and check for primes 

for number in numbers:
try:
    num = int(number.strip()) 
    if is_prime(num):
print(f"{num} is a prime number.") except ValueError:
print(f"Skipping invalid number: {number.strip()}")
except FileNotFoundError:


'''

arr = "  hai there, how you doin ?"
print(arr.split()) # splits based on spaces by default
print(arr.strip()) # removes \n and spaces from start and end 
print(arr.replace(" ","")) # removes all spaces by replacing with nothing