#print your name.
print("Hello, My name is Dhara")

#Add two numbers.
a=25
b=5
sum = a+b
print("sum = ",sum)

#Ask user name.

name=input("Enter your name: ")
print(name)

#simple calculator.

a=int(input("Enter a first num: "))
b=int(input("Enter a second num: "))

print("Addition :",a+b)
print("Substraction :",a-b)
print("Multification :",a*b)
print("divison :",a/b)

#print() Formating using sep and End.

print("Apple","Banana","Mango",sep="|",end="<--------End of the list\n")

# Formating msg for user input.

name=input("Enter your name: ")
age=int(input("Enter your age: "))
hobby=input("Enter your hobby: ")

print(f"I am {name}! at age {age}! my favorite hobby is {hobby}")

#Declare variable of diffrent data types and show thair types.

a=10
b=2.50
c="Python"
d=True

print(a,"Type",type(a))
print(b,"Type",type(b))
print(c,"Type",type(c))
print(d,"Type",type(d))

#python program.

subject1=input("Enter your subject1 name: ")
marks1=int(input("Enter your marks1: "))
subject2=input("Enter your subject2 name: ")
marks2=int(input("Enter your marks2"))
subject3=input("Enter your subject3 name: ")
marks3=int(input("Enter your marks3"))

Total=marks1+marks2+marks3
avrage=Total/3

if Total>=90:
    Grade="A"
elif Total>=75:
    Grade="B"
elif Total>=60:
    Grade="c"
elif Total>=45:
    Grade="d"
else:
    Grade="Fail"

print("--------------------Result-------------")

print(f"subject1: {subject1}\n")
print(f"subject2: {subject2}\n")
print(f"subject3: {subject3}\n")
print(f"marks1: {marks1}\n")
print(f"marks2: {marks2}\n")
print(f"marks3: {marks3}\n")
print(f"Total: {Total}\n")
print(f"avrage: {avrage}\n")
print(f"Grade: {Grade}\n")
