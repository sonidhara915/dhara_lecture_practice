# Basic pattern

# 1. Patterns (without space pattern)

size=5
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()

print("="*20)
        
#2. Right-Angled Triangle Pattern

size=5
for i in range(1,size+1):
    for j in range(i):
        print("*",end="")
    print()

print("-"*20)

#3. Inverted Right-Angled Triangle Patterns

size=5
for i in range(size,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print("="*20)
#4. Patterns (with space)

rows = 5

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  " , end="")
    for k in range(2 * i - 1):
        print("*" , end="")
    print()


for i in range(rows - 1 , 0 , -1):
    for j in range(rows - i):
        print("  " , end="")
    for k in range(2 * i - 1):
        print("*" , end="")
    print()

print("="*20)
#Diamond pattern

row=5

for i in range(1,row+1):
    print(" "*(row-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")
        
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")

