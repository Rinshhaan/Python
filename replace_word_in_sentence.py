# ALGORITHM
# STEP 1: Start.
# STEP 2: Input the sentence from the user.
# STEP 3: Input the word to be replaced and the new word. 
# STEP 4: Use the replace() function to replace the word. 
# STEP 5: Print the updated sentence.
# STEP 6: Stop.

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")

new_sentence = sentence.replace(old_word,new_word)

print("The new sentence is: ",new_sentence)

# or to refine we can use 
# import re
# if re.search(rf'\b{old_world}\b', sentence): now replace else dont
# \b helps to match whole words only    

# another way is to split sentences using split() 
# if old_word in sentence.split(): now replace else dont