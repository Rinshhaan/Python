# r -0 read , w - write , a - append , x - create file if not exists
# w+ - read and write (overwrites existing file)
# a+ - read and append (creates file if not exists)
# r+ - read and write (file must exist) 

file = open('writefile.txt','w')
file.write("Hello World\n")
file.write("This is AI lab file handling\n")
file.close() # don't forgewt to close else use with statement, there no need to close manually

with open('ha.txt','a') as file:
    file.write("Appending new line to the file\n")

with open('ha.txt','r') as file:
    content = file.read()
    print(content)

with open('writefile.txt','w+') as file:
    file.write("Overwriting the existing content\n")
    #file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print(content)