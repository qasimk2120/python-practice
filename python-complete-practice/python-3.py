#functions in python
#functions are actually objects in python

# def func():  # Function definition
#     print("This is a function")    # Function body
#     def inner_func():  # Nested function definition
#         print("This is an inner function")  # Nested function body
#     inner_func()  # Calling the nested function

# func()  # Calling the function
# # print(type(func))  # <class 'function'>


# def func(x, y):   # Function definition with parameters x and y   , arguments are the values passed to the function when it is called 
#     print('Run', x, y)  # Function body
#     return x * y, x / y  # Function returns the sum of x and y, # multiple return values are returned as a tuple
# # print(func(5, 6))  # Function call with arguments 5 and 6
# # result = func(3, 5)  # Function call with arguments 3 and 5
# # print(result)  # Output: 15
# # or 
# # result = func(5,6)  # Function call with arguments 5 and 6
#  # Output: 30

# r1, r2 = func(10, 2)  # Unpacking multiple return values into r1 and r2
# print(r1)  # Output: 20
# print(r2)  # Output: 5.0


# Default parameter values
# def func(x, y, z =None): # z has a default value of None
#     print('Run', x, y, z)  # Function body
#     return x+y, x / y  # Function returns the sum of x and y and the division of x by y

# r1, r2 = func(10, 2, 7)  # z takes the default value of None
# print(r1, r2)  # Output: 12


#unpack operator in function arguments, *args and **kwargs
  
# def func(x):   # Function definition with parameter x
#     def func2():    # Nested function definition
#         print(x)    # Accessing x from the outer function
#     return func2    # Returning the nested function
# func(3)()  # Output: 3   # Calling func with argument 3 and then calling the returned function

# print(func(3))  # Output: <function func.<locals>.func2 at ...>   # Calling func with argument 3 and printing the returned function object
# print(func(3)())  # Output: 3 and None   # Calling func with argument 3, calling the returned function, and printing the result


# x = func(3) # Calling func with argument 3 and storing the returned function in x
# x()  # Output: 3   # Calling the function stored in x



# def func(*args, **kwargs):  # Function definition with *args and **kwargs
#     pass

# x = [1, 23, 2234322, 2727]
# print(x)
# print(*x)  # Unpacking the list x into individual arguments , # Output: 1 23 2234322 2727  # equivalent to func(1, 23, 2234322, 2727)


# def func(x, y):
#     print(x, y)

# pairs = [(1, 2), (3, 4), (5, 6)]

# for pair in pairs:
#     # func(pair[0], pair[1])  # Unpacking each tuple in pairs into individual arguments for func, non-pythonic way
#     func(*pair)  # Unpacking each tuple in pairs into individual arguments for func, pythonic way


#unpacking dictionaries in function arguments

# def func(a, b, c):
#     print(a, b, c)
# data = {'a': 1, 'b': 2, 'c': 3}
# for data in [data]:
#     func(**data)  # Unpacking the dictionary data into keyword arguments for func

#     #double asterisks (**) are used to unpack dictionaries into keyword arguments in function calls, 
#     #single asterisk (*) is used to unpack iterables like lists or tuples into positional arguments.


# def func(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments", *args)
#     print("Keyword arguments:", kwargs)

# func(1,2,3,4,5,6, one=0, two=1)


#local and Global Scope
# x = 'tim'   # Global variable x
# def func(name):
#     # x = name  # Local variable x
#     global x  # Declare x as global to modify the global variable, never use this unless necessary, always ends up in a mess or hard to debug
#     x = name  # Modify the global variable x
#     print("Inside func:", x)  # Accessing local variable x
# func('alice')  # Calling func with argument 'alice'
# print("Outside func:", x)  # Accessing global variable x



#exceptions in python
# raise Exception("This is an exception BAD BAD BAD")  # Raising a generic exception with a custom message
# raise ValueError("This is a value error")  # Raising a ValueError with a custom message
# raise TypeError("This is a type error")  # Raising a TypeError with a custom message
# raise FileExistsError("This is a file exists error")  # Raising a FileExistsError with a custom message
# raise IndexError("This is an index error")  # Raising an IndexError with a custom


# #handling exceptions with try-except
# try:
#     x = 7 / 0
# except Exception as e:  #generic exception handler/catcher , could be more specific like ZeroDivisionError 
#     print("An error occurred:", e)  # Handling any exception and printing the error message
# finally:
#     print("This will always execute")  # This block will always execute regardless of whether an exception occurred or not
