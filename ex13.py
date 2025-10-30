# Write a program to replace a word by another word in a sentence
# and count the number of words in it.
import re


sentence = input("enter a sentence: ")
word = input("Enter a word to be replaced: ")

if re.search(rf'\b{word}\b',sentence):
    #print(re.search(rf'\b{word}\b',sentence))
    replace_word = input("Enter a word to be replaced: ")
    replaced_sentence = sentence.replace(word,replace_word)
    print(f"replaced sentence: {replaced_sentence}")
    count_ = replaced_sentence.split()
    print(len(count_))
else:
    print("No matching word found")

