# #Ask user for their name
# #input function to take in input from users

# #name is a variable we creater 
# #str for string , actual type of data
# name =input("What is your name? ")

# #Say Hello to user, print function to show something to user
# #print takes multiple arguments, variables
# # print("hello, ", end="");
# # print(name)

# #using sep
# print("Hello,", name, sep='')
# """Multi-Line Comments"""

# #two types of  arguments
# #positional arguments
# #named arguments

#we can use \ which is the escape character and is useful for below scenario
# print("hello, \"friend\"")

#new feature in python, newer method of formatting strings in python
# name =input("What is your name? ")
# print(f"hello, {name}")

#.strip()  is used remove extra whitespace from a string  
# name =input("What is your name? ")
# name = name.strip()
# print(f"hello, {name}")

#.capitalize() is used to capitalize the first letter of a string
# name =input("What is your name? ")
# name = name.capitalize()
# print(f"hello, {name}")

#.title() is used to title the first letter of every word in a string
# name =input("What is your name? ")
# name = name.title()
# print(f"hello, {name}")

#funtions can be chained together 
# name =input("What is your name? ").strip().title()
# print(f"hello, {name}")

#split function  splits a string into multiple smaller substrings
# name =input("What is your name? ").strip().title()
# first, last = name.split(' ')
# print(f"hello, {first}")

#int is short for integer in python, we can +, - , *, /, %
#float is used for  decimal point decimal points

#using int for adding numbers as user input is taken as string 
# x = int(input('Whats x? '))
# y = int(input('Whats y? '))
# print(x + y)

#using float for adding numbers in terms of floating point numbers
#.round(number[, ndigits]) function is used to round numbers 
# x = float(input('Whats x? '))
# y = float(input('Whats y? '))
# z = round(x+ y)
# print(f"{z:,}")

#rounding decimal points
# x = float(input('Whats x? '))
# y = float(input('Whats y? '))
# z = x/y
# # z = round(x /y, 2)
# print(f"{z:.2f}") #cryptic method using f string to show upto two decimal points

#defining functions, al of the indented code after the function defintion should be in line


# def main(): #not required but for data convention, this tells the reader that this is the 
#     #main part of the code, we must call this function somehwhere otherwise python won't 
#     #know about it 
#     name = input("What's your name? ")
#     hello(name) #name is passed to to variable and returned from the function 

# def hello(to="world"): #here we set a default value i.e. ="world"
#     print("Hello, ", to)

# main()
# #in python function must exist by the time you are calling it
# #scope refers to a variable only existing or avaible in the context in which you defined it





# x = float(input('Whats x? '))
# y = float(input('Whats y? '))
# z = round(x+ y)
# print(f"{z:,}")

def main():
    x =  int(input("What's x? "))
    print("x squared is ", square(x))
def square(n):
    # return n * n #here we also have pow function to calculate power of a number e.g.
    return n * n
if __name__ == "__main__":
    main()