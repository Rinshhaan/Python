""""ALGORITHM
Step 1: Initialize Counters:
•Set word_count to 0.
•Set sentence_count to 0.
•Set uppercase_count to 0.
•Set lowercase_count to 0.
•Set special_count to 0.

Step 2: Open the File:
•Open the file using the file path provided.
•Read the content of the file into a variable (e.g., text).

Step 3:Count Sentences:
•Initialize sentence_count to 0.
•For each character in text, check if the character is a sentence-ending punctuation mark (., !, or ?):
o If it is, increment sentence_count.

Step 4: Count Words:
•Use the split() function to split the text into words.
•Count the number of words in the resulting list and store it in word_count.

Step 5: Count Uppercase and Lowercase Letters:
•Initialize uppercase_count and lowercase_count to 0.
•For each character in text:
oIf the character is an uppercase letter (use char.isupper()), increment uppercase_count.
oIf the character is a lowercase letter (use char.islower()), increment lowercase_count.

Step 6: Count Special Symbols:
•Initialize special_count to 0.
•For each character in text:
oIf the character is a special symbol (i.e., any punctuation character), increment special_count.

Step 7:Print the Results:
•Print the values of word_count, sentence_count, uppercase_count, lowercase_count, and special_count.

Step 8: Stop.
"""""

import string

def count_file_details(file_path):
    # Initialize counters
    word_count = 0
    sentence_count = 0
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0  # elif char in string.punctuation
    
    # Open the file
    with open(file_path, 'r') as file:
        text = file.read()   # Read the entire file content as a single string
        print(f"{text}")


        # Count sentences (using ., !, ?)
        sentence_count = text.count('.') + text.count('!') + text.count('?')

        # Split text into words
        words = text.split()    # ['ha', 'saaa', 'a', '333', '44', '?', '11', '12', '3', '000', 'haz']
        word_count = len(words)

        # Count uppercase, lowercase, and special characters
        for char in text:  # or word
            print(f"{char}")
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char in string.punctuation:
                # print(char.isupper()) returns false or true
                special_count += 1

    # Print the results
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    print(f"Uppercase letter count: {uppercase_count}")
    print(f"Lowercase letter count: {lowercase_count}")
    print(f"Special symbol count: {special_count}")


# Example usage
file_path = 'ha.txt'
count_file_details(file_path)

