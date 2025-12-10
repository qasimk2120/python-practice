#Optional Parameters  in Python
# In Python, you can define functions with optional parameters by providing default values for those parameters. 
# If the caller does not provide a value for an optional parameter, the default value is used.

# def func(x=1):  # x is an optional parameter with a default value of 2 , for example the user doesn't provide any value when calling the function

#     return x **2

# # call = func(5)
# # print(call)  # Output: 25
# call = func()  # Here, the user doesn't provide any value, so the default value of 1 is used
# print(call)  # Output: 1


#you can also have multiple optional parameters in a function:

# def func (word, frequency = 1, add = 5):   # frequency is an optional parameter with a default value of 1
#     print(word * (frequency + add) )
# call = func('hello', 5)  # Here, both parameters are provided by the user



# class car(object):   # Define a class named 'car'
#     def __init__(self, make, model, year, condition= 'New', kms=0):  # condition and kms are optional parameters with default values
#         self.make = make   # Required parameter
#         self.model = model  # Required parameter
#         self.year = year  # Required parameter
#         self.condition = condition # Optional parameter with default value 'New'
#         self.kms = kms # Optional parameter with default value 0
#     def display_info(self, showAll=True):  # showAll is an optional parameter with default value True, and the method displays car information
#         if showAll:
#             print("This car is a %s %s from %d in %s condition with %d kms." % (self.make, self.model, self.year, self.condition, self.kms))
#         else:
#             print("This car is a %s %s from %d." % (self.make, self.model, self.year))

# whip = car("Toyota", "Corolla", 2020) # Create a car object with default condition and kms
# whip.display_info(False)  # Show only make, model, and year
# whip.display_info()  # Show all information about the car





#Static and Class Methods in Python
# In Python, static methods and class methods are two types of methods that belong to a class rather than an instance of the class.
# Static Methods: Static methods are methods that do not require access to the instance (self) or class (cls) and are defined using the @staticmethod decorator.
# They are used for utility functions that are related to the class but do not need to access or modify class or instance data.
# Class Methods: Class methods are methods that have access to the class itself and are defined using the @classmethod decorator.
# They take the class (cls) as the first parameter instead of the instance (self) and are often used for factory methods or methods that operate on class-level data.


# class person(object):
#     population = 50  # Class variable to keep track of population
#     def __init__(self, name, age):   # Instance method to initialize name and age
#         self.name = name
#         self.age = age
    
#     @classmethod  # Class method to get population , class method can be called on any instance of the class, no need to create a seperate instance/object
#     #no need of self parameter here instead we use cls to refer to the class itself
#     def getPopulation(cls):  # Class method to get population
#         return cls.population       # Access class variable using cls
    
#     @staticmethod  # Static method to check if a number is valid age
#     #similar to class method we don't use self or cls here, it doesnt access instance or class data, and doesnt neeed any parameters
#     #static method cannot access or modify class or instance for example the population variable here 

#     def isAdult(age):  # Instance method to check if the person is an adult
#         return age >= 18  # Check if age is 18 or older
#     def displayInfo(self):  # Instance method to display person's information
#         print(self.name, 'is', self.age, 'years old.')


# newPerson = person('Alice', 30)  # Create a new person instance
# print(person.isAdult(5)) # Call class method to get population




#map function in Python
# The map() function in Python is a built-in function that applies a given function to each item in an iterable (like a list or tuple) and returns an iterator (map object) with the results.
# the problem that map function solves is to apply a specific operation or transformation to each element of a collection without using explicit loops.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):   # Function to square a number
    return x ** x

# newList = []
# for x in li:
#     newList.append(func(x))  # Apply func to each element and append to newList

# print(newList)  # Output the new list

# Using map function to achieve the same result
# print(list(map(func, li)))

print([func(x) for x in li if x%2==0])  # Using list comprehension to achieve the same result

