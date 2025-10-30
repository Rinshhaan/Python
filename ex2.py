# Q) write a python program to replace all the spaces in the input string with * and put $ at the start and end of the string.Input string is stored in a text file

file = open('ex.txt','r')
content = file.read() # read all as string
file.close() # close here

replaced_content = content.replace(" ","*") #("\n","*") removes newline make to single line
print(replaced_content)

final_content = "$"+replaced_content+"$"



with open('ex.txt','w') as file:
    file.write(f"replaced: { final_content}")