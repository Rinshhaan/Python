# A set of numbers are stored in a file. Write a program to find the sum of odd and even numbers from the given numbers

file = open('exnum.txt','r')
content = file.read()
file.close()

numbers = list(map(int,(content.split()))) # dont forget ,
print(content.split())
print(numbers)

odd_num = [num for num in numbers if num % 2 != 0]
even_num = [num for num in numbers if num % 2 == 0]

print("odd numbers: ",odd_num)
print("even numbers: ",even_num)
