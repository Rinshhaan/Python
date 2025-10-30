sentence = "i am coding in python"

print(sentence.capitalize())  # I am coding in python

print(sentence.split()) # ['i', 'am', 'coding', 'in', 'python']
print(sentence.upper())  # I AM CODING IN PYTHON
print(sentence.lower())  # i am coding in python
print(sentence.title())  # I Am Coding In Python
print(sentence.find("coding"))  # 5 - return index where substring starts
print(sentence.replace("python", "Java"))  # i am coding in Java
print(sentence.count("i"))  # 2 - count occurrences of substring
print(sentence.startswith("i am"))  # True
print(sentence.endswith("python"))  # True
print(sentence.isalpha())  # False - because of spaces
print(sentence.isdigit())  # False
print(sentence.strip())  # removes leading/trailing whitespace
print(sentence.index("in"))  # 14 - return index where substring starts, raises error if not found
print(sentence.rfind("i"))  # 10 - return highest index of substring
print(sentence.lstrip())  # removes leading whitespace
print(sentence.rstrip())  # removes trailing whitespace 
print(sentence.join(["Hello", "World"]))  # Helloi am coding in pythonWorld
print(len(sentence))  # 22 - length of the string   

