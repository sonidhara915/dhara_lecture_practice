# 1. if statement

age=20
if age>=18:
    print("you are eligible to vote")

# 2. if...else statement

num=5
if num>=0:
    print("Positive")
else:
    print("Negetive")

# 3. if...elif..else statment

mark=int(input("Enter your num : "))

if mark>=90:
    grade = "A"
elif mark>=75:
    grade = "B"
elif mark>=45:
    grade = "C"
else:
    grade = "Fail"

print("your grade = ",grade)

# 4. match statement

char="a"

match char:
    case "a"|"e"|"i"|"o"|"u":
        print("Vowel")
    case _:
        print("Consonant")
