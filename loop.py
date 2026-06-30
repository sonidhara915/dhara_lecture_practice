#while loop.

i=1
while i<=5:
    print(i)
    i+=1

print(".........Revers loop.........")
    
i=5
while i>=1:
    print(i)
    i-=1

#for loop.
# Use in
'''
range
list
tuple
string
'''

print("-----for loop------")
for i in range(1,6):
    print(i)

#revers for loop

print("-----revers for loop-----")
for i in range(5,0,-1):
    print(i)

#loop through string

print("-----string loop-----")
name="python"
for i in name:
    print(i,end="")

#loop through list

print("\n-----list loop-----")

fruits=["apple","banana","mango","kivi"]

for i in fruits:
    print(i)

#range function

print("-----range types----")

for i in range(5):
    print(i)

print("-----------------")

for i in range(1,6):
    print(i)

print("----------------")

for i in range(1,11,2):
    print(i)

print("-"*20)

for i in range(1,11,3):
    print(i)

print("-"*20)

for i in range(10,0,-1):
    print(i)

#nasted loop.

print("-"*20)

for i in range(1,6):
    for j in range(1,4):
        print(j,end="")
    print()

# brake statment

print("-"*20)
for i in range(1,6):
    if i==4:
        break
    print(i)

#continue statement

print("-"*20)
for i in range(1,6):
    if i==4:
        continue
    print(i)

#pass

print("-"*20)
for i in range(1,6):
    if i==4:
        pass
    print(i)
    
