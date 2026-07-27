# Create and Diaplay 2D Arrays
'''
matrix = []

for i in range(3):
    row = list(map(int , input(f" Enter Row {i + 1} :").split()))
    matrix.append(row)
    
for row in matrix:
    for value in row:
        print(value , end=", ")
    print()

for row in matrix:
    print(row , end=",\n")


for row in matrix:
    print("[" , end="")
    print(*row , sep=" , " , end="")
    print("]")
    
print(matrix)
'''

matrix = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

print(matrix[0][0])

print(matrix[1][1])

# Create 2D Array in 3x3 Matrix
'''
matrix = []

for i in range(3):
    row = list(map(int , input(f"Enter Row {i + 1} : ").split()))

    matrix.append(row)

print("Matrix:")

for row in matrix:
    for value in row:
        print(value , end="\t")

    print()

print(matrix)


print(matrix[0][0])
print(matrix[2][2])

'''

# Transpose of 2 x 3 Matrix
'''
matrix = []

for i in range(2):
    
    row = list(map(int , input(f"Enter Row {i + 1} : ").split()))

    matrix.append(row)

print(matrix)

transpose = []

for j in range(3):

    temp = []

    for i in range(2):

        temp.append(matrix[i][j])

    transpose.append(temp)

print(transpose)

for row in transpose:

    print(row)

'''

# Sum of all Matrix Values

rows = int(input("Enter Number of rows:"))
cols = int(input("Enter Number of columns:"))

matrix = []

for i in range(rows):

    row = list(map(int , input(f"Enter Row {i + 1} :").split()))
    '''
    if len(row) == cols:
        matrix.append(row)
        break

    else:
        print("Please Enter exactly values.")
    '''
    matrix.append(row)
        
print(matrix)

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)
