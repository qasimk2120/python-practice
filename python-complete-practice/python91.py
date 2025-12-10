# #class and static methods in python
# # @classmethod and @staticmethod are decorators used to define class methods and static methods respectively. 
# # Class methods take cls as the first parameter and can access class variables, 
# # #while static methods do not take self or cls as the first parameter and cannot access class or instance variables.
# class Dog:
#     dogs = []
#     XC = 5
#     def __init__(self, name):
#         self.name = name
#         Dog.dogs.append(self)
#     @classmethod  #class method , #it takes cls as first argument , #it can access class variables
#     #can simply be called on the name of the class
#     def num_dogs(cls): 
#         return len(cls.dogs)
    
#     @staticmethod   #static method , #it doesn't take self or cls as first argument , #it can't access class or instance variables
#     #static methods don't need a class or instance reference, so they can be called on the class name directly
#     #no need of self or cls parameter
#     def bark(n):
#         #BARK n times
#         for _ in range(n):
#             print("Bark!")
# # tim = Dog("Tim")
# # jim = Dog("Jim")
# # print(Dog.num_dogs())  #Output: 2

# Dog.bark(3)  #Output: Bark! Bark! Bark!

#private and Public Classes in Python
  #private class, #by convention, a class whose name starts with an underscore is considered private and should not be accessed directly from outside the module
    #in python, there is no strict enforcement of private classes, but the underscore convention is widely followed
    #private classes are typically used for internal implementation details that are not meant to be part of the public API
    #they can still be accessed if needed, but it is discouraged
    #private classs are often used in conjunction with public classes to encapsulate functionality
class _Private: 
    def __init__(self, name):
        self.name = name
class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)
    def _display(self):
        print("Hello")
    
    def display(self):
        print("Hi")