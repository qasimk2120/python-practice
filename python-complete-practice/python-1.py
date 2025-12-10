# #Data Types

# #INT 
# #An integer is a whole number, positive or negative, without decimals.
# -267236
# 76373

# #FLOAT
# #A float is a number, positive or negative, containing one or more decimals.
# 3.14159
# -0.001
# 2727.0  

# #STRING
# #A string is a sequence of characters, enclosed in single or double quotes.
# "Hello, World!"
# 'Python is fun'
# '12345'  # This is a string, not a number

# #BOOLEAN
# #A boolean represents one of two values: True or False.
# True
# False

# #Output and Printing
# print("Integer:", 42)
# print("Float:", 3.14)
# print("String:", "Hello, Python!")
# print("Boolean:", True)
# print("Sum of 5 and 10 is:", 5 + 10)

# # print configuration 
# print("hello", 'end', 87, False, end='\n', sep='---')


# #variables
# #A variable is a named location used to store data in memory.
# age = 25
# name = "Alice"
# is_student = True
# height = 5.7
# print("Name:", name)
# print("Age:", age)
# print("Is Student:", is_student)
# print("Height:", height)
# # You can change the value of a variable
# age = 26
# print("Updated Age:", age)
# # Variable names should start with a letter or underscore and can contain letters, numbers, and underscores.
# #Variable names cannot start with a number or contain spaces.
# # Variable names should be descriptive.
# # They are case-sensitive (e.g., age and Age are different variables).
# _first_name = "John"
# lastName = "Doe"
# print("First Name:", _first_name)
# print("Last Name:", lastName)
# # Avoid using reserved keywords as variable names (e.g., print, if, else, etc.).
# # Example of invalid variable names (uncommenting these will cause errors)
# # 1st_name = "Invalid"  # Starts with a number
# # class = "Invalid"     # 'class' is a reserved keyword
# # full name = "Invalid"  # Contains a space
# full_name = "John Doe"  # Correct way without space


#Getting User Input
# The input() function reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello,", name + "!", "You are", age, "years old.")

# Arithmetic Operations
# x = 10
# y = 3
# print("Addition:", x + y)          # Addition
# print("Subtraction:", x - y)       # Subtraction
# print("Multiplication:", x * y)    # Multiplication
# print("Division:", x / y)          # Division (float)   # Division always returns a float 
# print("Floor Division:", x // y)   # Floor Division   # Floor division returns the largest integer less than or equal to the division result
# print("Modulus:", x % y)           # Modulus      # Modulus returns the remainder of the division
# print("Exponentiation:", x ** y)   # Exponentiation    # Exponentiation raises x to the power of y

# #you cannot perform arithmetic operations directly on strings and numbers
# # name = "Alice"
# # age = 25
# # print(name + age)  # This will raise a TypeError
# # To perform arithmetic operations with user input, you need to convert the input strings to numbers.
# # age = int(input("Enter your age: "))  # Convert input to integer
# # height = float(input("Enter your height in meters: "))  # Convert input to float
# # print("Next year, you will be", age + 1, "years old.")
# # print("In 5 years, you will be", age + 5, "years old.")



#BEDMAS Rule
# BEDMAS stands for Brackets, Exponents, Division and Multiplication, Addition and Subtraction. It is the order of operations used to solve mathematical expressions.
# result = (3 + 5) * 2 ** 2 / 4 - 1
# print("Result of the expression is:", result)
# # Step-by-step breakdown:
# # 1. Brackets: (3 + 5) = 8
# # 2. Exponents: 2 ** 2 = 4
# # 3. Multiplication: 8 * 4 = 32
# # 4. Division: 32 / 4 = 8.0
# # 5. Subtraction: 8.0 - 1 = 7.0
# # Final result: 7.0

#int to float conversion,  float to int conversion, int to string conversion, string to int conversion
# num = input("Enter a number: ")
# num_int = int(num)  # Convert string to integer
# num_float = float(num)  # Convert string to float
# num_str = str(num)  # Convert to string (though it's already a string from input)
# print("Integer:", num_int)
# print("Float:", num_float)
# print("String:", num_str)   

# string methods 
# hello = "hello"
# print(type(hello))  # Output: <class 'str'>
# print(hello.upper())  # Output: "HELLO"
# print(hello.capitalize())  # Output: "Hello"    
# print(hello.replace("l", "p"))  # Output: "heppo"
# print(hello.count("l"))  # Output: 2
# print(hello.find("e"))  # Output: 1
# print(hello.isalpha())  # Output: True
# print(hello.isdigit())  # Output: False
# print(hello.split("e"))  # Output: ['h', 'llo']
# print(hello.strip())  # Output: "hello" (removes leading/trailing whitespace)
# print(hello.startswith("he"))  # Output: True
# print(hello.endswith("lo"))  # Output: True
# print(hello.swapcase())  # Output: "HELLO"
# print(hello.zfill(10))  # Output: "00000hello"
# print(hello.center(20, '*'))  # Output: "*******hello********"
# print(hello.rjust(15))  # Output: "          hello"
# print(hello.ljust(15, '-'))  # Output: "hello----------"
# print(hello.encode())  # Output: b'hello'
# print(hello.format())  # Output: "hello"
# print(hello.islower())  # Output: True
# print(hello.isupper())  # Output: False
# print(hello.title())  # Output: "Hello"


#string addition and multiplication
# str1 = "Hello"
# str2 = "World"
# print(str1 + " " + str2)  # String Addition (Concatenation)
# print(str1 * 3)  # String Multiplication (Repetition)



#conditional operators
# ==  # Equal to
# !=  # Not equal to
# >   # Greater than
# <   # Less than
# >=  # Greater than or equal to
# <=  # Less than or equal to
# x = 'hello'
# y = 'hello'
# print(x == y)  # True
# print(x != y)  # False
# print('a' > 'z') # False (based on ASCII values)
# print('a' < 'z') # True (based on ASCII values)

#chained conditionals    # are used to evaluate multiple conditions in a single statement.
# x = 7
# y = 8
# z = 0

# result1 = x ==y # False
# result2 = y >x # True
# resyult3 = z < x + 2 # True

# #logical operators
# # and  # Returns True if both statements are true
# # or   # Returns True if one of the statements is true
# #not  # Reverse the result, returns False if the result is true
# #order of precedence: not, and, or
# print(result1 and result2)  # False
# print(result2 or result1)   # True
# print(not result1)          # True

#if else statements
# x =  input("Name: ")
# if x == "Alice":
#     print("you are great")
# elif x == "Bob":
#     print("bye Bob")


#collections in python
#LIST  with square brackets [] , ordered, mutable (changeable), allows duplicate elements , indexed, can contain mixed data types
x =  [4, "hello", 3.14, True, 4]
print(len(x))  # Length of the list
print(x[1])    # Accessing elements by index
x.append("new item")  # Adding an element to the end
print(x)
x.remove(4)   # Removing the first occurrence of an element
print(x)
x.pop()       # Removing an element by index, default is the last element, if index is not specified , can also specify index inside pop()
print(x)
x[0] = 10  # Modifying an element
print(x)