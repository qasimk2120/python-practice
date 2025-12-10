# # # # #objects in python

# # # # x= 5   #here x is the instance of int class
# # # # y = 'string'  # here y is the instance of str class
# # # # #these classes allow  us to have build in functionalities
# # # # h = int(y)  #someone built int class and defined how to convert str to int
# # # # y.strip()    #someone built str class and defined how to strip spaces from string 
# # # # print (type(x))
# # # # print (type(y))
# # # #if i call .upper() on x it will give error because int class does not have upper method 
# # # #print(y.upper())  # here upper is the method of str class which is used to convert string to uppercase
# # # # import turtle

# # # # tim = turtle.Turtle()  # here tim is the instance of Turtle class
# # # # tim.color("red")      # here color is the method of Turtle class which is used to set the color of the turtle
# # # # tim.forward(100)      # here forward is the method of Turtle class which is used to move the turtle forward by a certain distance
# # # # tim.right(90)        # here right is the method of Turtle class which is used to turn the turtle right by a certain angle
# # # # tim.forward(100)
# # # # turtle.done()
# # # # # someone built Turtle class and defined how to create a turtle and how to move it around the screen
# # # x =5
# # # y = 'string'
# # # print(y.replace('s',''))  # here replace is the method of str class which is used to replace a substring with another substring
# # # def func(x):
# # #     return x + 1
# # # print(func(5))



# # #CREATING OUR OWN CLASS in python

# # class Dog:   # here we are creating a class named Dog
# #     def __init__(self, name, age): #constructor method to initialize the object, # needs to be in most of the classes #name is a parameter 
# #         #in classes we have methods and attributes, methods are functions defined inside the class and attributes are variables defined inside the class
# #         #to create an attribute we use self keyword
# #         self.name = name  # here name is an attribute of the Dog class    , #self means the current instance of the class, it belongs to the object being created
# #         self.age = age    # here age is another attribute of the Dog class
# #         self.li = [1,2, 3, 4] # here li is another attribute of the Dog class which is a list


# #     def speak(self):   #method of the Dog class
# #         print("Hi I am " + self.name + " and I am " + str(self.age) + " years old.")     # we can define the behavior of the dog here
    
# #     def talk(self):
# #         print("Bark! Bark!")


# # # class Cat:
# # #     def __init__(self, name, age, color):
# # #         self.name = name
# # #         self.age = age
# # #         self.color = color

# # #     def meow(self):
# # #         print("Meow! I am " + self.name + 'and i am ' + self.age + ' years old and my color is ' + self.color)
# # #we do not need to create multiple classes for similar objects, we can use inheritance to create a base class and then create subclasses that inherit from the base class

# # class Cat(Dog):  # here cat class is inheriting from Dog class
# #     def __init__(self, name, age, color):
# #         super().__init__(name, age)  # calling the constructor of the Dog class
# #         self.color = color  # adding color attribute to the Cat class
# #     def talk(self):
# #         print("Meow! Meow!")      #anything we do in the inherited class will override the parent class method if the method name is same
# # jim = Dog('Jim', 8)  # here jim is the instance of Dog class
# # jim.speak()  # calling the speak method of the Dog class for jim instance
# # jim.talk()  # calling the talk method of the Dog class for jim instance
# # tim = Cat('tim', 5, 'black')  # here tim is the instance of Cat class
# # tim.speak()  # calling the speak method of the Dog class for tim instance
# # tim.talk()  # calling the talk method of the Cat class for tim instance
# class Vehicle():
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color = color
#     def fillUpTank(self):
#         self.gas = 100
#     def emptyTank(self):
#         self.gas = 0
#     def gasLeft(self):
#         return self.gas

# class car(Vehicle):
#     def __init__(self, price, gas, color,speed):
#         super().__init__(price, gas, color)
#         self.speed = speed
#     def beep(self):
#         print("Beep! Beep!")

# class Truck(car):
#     def __init__(self, price, gas, color,tires):
#         super().__init__(price, gas, color)
#         self.tires = tires
#     def beep(self):
#         print("Honk! Honk!")

#overloading default python methods
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x , y):
        self.x += x
        self.y += y
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y)
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p): 
        return self.length() > p.length()
    def __ge__(self, p):
        return self.length() >= p.length()
    def __le__(self, p):
        return self.length() <= p.length()
    def __lt__(self, p):
        return self.length() < p.length()
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1,3)
p4 = Point(0,1)
# p5 = p1 + p2
# p6 = p4 - p1
# p7 = p2 * p2
# print(p5, p6, p7)

print(p1 > p2)  #True
print(p1 < p2)  #False
print(p1 >= p2)  #True
print(p1 <= p2)  #False
print(p1 == p2)  #False
print(p3 == p4)  #False
print(p1)  #(3, 4)