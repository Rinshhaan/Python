# ALGORITHM
# STEP 1: Start.
# STEP 2: Input two matrices as nested lists.
# STEP 3: Verify the dimensions of the matrices are the same. 
# STEP 4: Add corresponding elements of the matrices.
# STEP 5: Print the resulting matrix. 
# STEP 6: Stop

rows,cols = map(int,input("Enter number of rows and columns separated by space: ").split())

# Input the first matrix
print("Enter elements of the first matrix:")
matrix1 = [[int(input()) for _ in range(cols)] for _ in range(rows)]
print(matrix1)

# Input the second matrix
print("Enter elements of the second matrix:")
matrix2 = [[int(input(f"enter {i}th element of {j}th row: ")) for i in range(cols)] for j in range(rows)]

# Add the matrices
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

print("Resultant Matrix:")
for row in result:
    print(row)

# iteration = ['hai' for _ in range(5)]
# print(iteration)



arr = []
for i in range(2):
    for j in range(2):
        row = []
        num = int(input("Enter number: "))
        row.append(num)
    arr.append(row)
for i in range(2):
    for j in range(2):
        print(arr[i][j])