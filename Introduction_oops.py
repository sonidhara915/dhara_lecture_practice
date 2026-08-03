print("-"*20)
print("simple example of opps consept")
print("-"*20)

class car:

    #constucter
    
    def __init__(self,brand,model,color,price):

        self.brand = brand
        self.model = model
        self.color = color
        self.price = price


    def start(self):

        print(f"car {self.brand} {self.model} is starting....")

    def car_display(self):

        print(f"""
            Brand : {self.brand}
            Model : {self.model}
            Color : {self.color}
            Price : {self.price}
        """)

car1=car("Maruti Suzuki","WagonR","White",499000)

car1.start()
car1.car_display()

print("-"*20)
print("User example")
print("-"*20)

class student:

    #constucter

    def __init__(self,name,age,course,marks):

        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def user_display(self):

        print(f"""
            Name : {self.name}
            Age : {self.age}
            Course : {self.course}
            Marks : {self.marks}
        """)
        
student1 = student("Dhara",24,"Python",87)

student1.user_display()

print("-"*20)
print("Merge above examples")
print("-"*20)

class car:

    def __init__(self,brand=None,model=None,color=None,price=None,name=None,age=None,course=None,marks=None):

        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def car_display(self):

        print(f"""
            Brand : {self.brand}
            Model : {self.model}
            Color : {self.color}
            Price : {self.price}
        """)

    
    def user_display(self):

        print(f"""
            Name : {self.name}
            Age : {self.age}
            Course : {self.course}
            Marks : {self.marks}
        """)

car1 = car("Maruti Suzuki","WagonR","White",499000)
student1 = car("Dhara",24,"Python",87)


car1.car_display()
student1.car_display()

print("-"*20)
print("simple example")
print("-"*20)

class person:

    name = "Dhara"

    age = 14

p1 = person()

print(type(p1))

print(p1.name)

print(p1.age)








