# # # #objects in python

# # # x= 5   #here x is the instance of int class
# # # y = 'string'  # here y is the instance of str class
# # # #these classes allow  us to have build in functionalities
# # # h = int(y)  #someone built int class and defined how to convert str to int
# # # y.strip()    #someone built str class and defined how to strip spaces from string 
# # # print (type(x))
# # # print (type(y))
# # #if i call .upper() on x it will give error because int class does not have upper method 
# # #print(y.upper())  # here upper is the method of str class which is used to convert string to uppercase
# # # import turtle

# # # tim = turtle.Turtle()  # here tim is the instance of Turtle class
# # # tim.color("red")      # here color is the method of Turtle class which is used to set the color of the turtle
# # # tim.forward(100)      # here forward is the method of Turtle class which is used to move the turtle forward by a certain distance
# # # tim.right(90)        # here right is the method of Turtle class which is used to turn the turtle right by a certain angle
# # # tim.forward(100)
# # # turtle.done()
# # # # someone built Turtle class and defined how to create a turtle and how to move it around the screen
# # x =5
# # y = 'string'
# # print(y.replace('s',''))  # here replace is the method of str class which is used to replace a substring with another substring
# # def func(x):
# #     return x + 1
# # print(func(5))



# #CREATING OUR OWN CLASS in python

# class Dog:   # here we are creating a class named Dog
#     def __init__(self, name, age): #constructor method to initialize the object, # needs to be in most of the classes #name is a parameter 
#         #in classes we have methods and attributes, methods are functions defined inside the class and attributes are variables defined inside the class
#         #to create an attribute we use self keyword
#         self.name = name  # here name is an attribute of the Dog class    , #self means the current instance of the class, it belongs to the object being created
#         self.age = age    # here age is another attribute of the Dog class
#         self.li = [1,2, 3, 4] # here li is another attribute of the Dog class which is a list


#     def speak(self):   #method of the Dog class
#         print("Hi I am " + self.name + " and I am " + str(self.age) + " years old.")     # we can define the behavior of the dog here

#     def change_age(self, new_age):  # another method of the Dog class to change the age of the dog
#         self.age = new_age  # changing the age attribute of the Dog class
    
#     def add_weight(self, weight):  # another method of the Dog class to add weight attribute
#         self.weight = weight  # adding weight attribute to the Dog class

# dog1name = 'Tim'  # variable to store the name of the dog
# dog1age = 12      # variable to store the age of the dog


# tim = Dog('Tim', 12)  # here tim is the instance of Dog class
# fred = Dog('Fred', 10)  # here fred is another instance of Dog class
# tim.change_age(13)  # calling the change_age method of the Dog class for tim instance
# tim.add_weight(30)  # calling the add_weight method of the Dog class for tim instance
# tim.speak()  # calling the speak method of the Dog class for tim instance
# fred.speak()  # calling the speak method of the Dog class for fred instance
# print(tim.name)
# print(tim.li)
# print(tim.weight)
# print(fred.weight)  # this will give error because fred instance does not have weight attribute