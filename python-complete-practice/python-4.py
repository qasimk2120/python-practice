#lambda functions in python
# lambda arguments: expression
# They are used for creating small, anonymous functions at runtime.
# They can have any number of arguments but only one expression.
# lambda is a 1 line annonymous function, # useful for short operations where defining a full function is unnecessary.

# x =  lambda a: a + 5  # Lambda function that adds 5 to the input/ this is not the advised way to define functions, use def for normal functions

# print(x(10))  # Output: 15   # Calling the lambda function with argument 10 and printing the result


# y = lambda a, b: a * b  # Lambda function that multiplies two inputs
# print(y(2, 3))  # Output: 6   # Calling the lambda function with arguments 2 and 3 and printing the result


# #MAP and FILTER functions using in python which use lambda functions 
# x = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
# mp = map(lambda i: i + 2, x)  # Using map with a lambda function to double each element in the list x
# print(list(mp))  # Output: [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
# #map applies the given function to each item of an iterable (like a list) and returns a map object (an iterator).
# #filter function applies a function to each item of an iterable and returns only those items for which the function returns True.
# np = filter(lambda i: i % 2 == 0, x)  # Using filter with a lambda function to get even numbers from the list x
# print(list(np))  # Output: [2, 4, 8, 10]

# x = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]



#F strings in python
# F-strings, or formatted string literals, are a way to embed expressions inside string literals, using curly braces {}.
# They are prefixed with the letter 'f' or 'F' before the opening quotation mark.
name = "Alice"
age = 30
# Using f-strings to format a string with variables
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.