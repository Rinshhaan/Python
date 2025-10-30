# ALGORITHM
# STEP 1: Start.
# STEP 2: Input the email ID from the user.
# STEP 3: Check if the email ID contains 'exactly one '@'' and has a valid domain. 
# STEP 4: Use a regular expression to validate the format.
# STEP 5: Print if the email ID is valid or not. STEP 6: Stop.


import re  #regular expression
email = input("Enter your email: ")
pattern =  r'^[\w\.-]+@[\w\.-]+\.\w+$' 

# print(f'{re.match(pattern,email)}')

if re.match(pattern,email): # re.match(pattern,string)
    print("valid email")
else:
    print("Not valid email")

# Explanation of the regex pattern:
# ^ asserts the start of the string.
# \w matches any word character (equivalent to [a-zA-Z0-9_]).
# \. matches a literal dot.
# \.- matches a literal dot or hyphen.
# + means one or more of the preceding element.
# @ matches the '@' symbol.
# [\w\.-] contains word characters, dots, or hyphens.
# $ asserts the end of the string.


# r'^[\w\.-]'+@[\w\.-]+\.\w+$'
