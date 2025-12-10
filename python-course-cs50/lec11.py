# #auto filter duplicates
# #using a set to store unique house names
# #then sort and print them
# students = [
#     {"name": "Hermione", "home": "Gryffindor"},
#     {"name": "Harry", "home": "Gryffindor"},
#     {"name": "Ron", "home": "Gryffindor"},
#     {"name": "Draco", "home": "Slytherin"},
#     {"name": "Padma", "home": "Ravenclaw"},

# ]

# houses = set()

# for student in students:
#     houses.add(student["home"])
# for house in sorted(houses):
#     print(house)


# #global variable vs instance variable
# # if a variable is defined outside all functions and classes, it is a global variable
# # if a variable is defined inside a class, it is an instance variable
# # global variable is shared across all instances of the class
# # instance variable is unique to each instance of the class


# #bank.py

# balance = 0  #global variable

# def main():
#     print(f"Balance is ${balance}")
#     deposit(100) 
#     withdraw(50)
#     print(f"Balance is ${balance}")



# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n
# if __name__ == "__main__":
#     main()


#object oriented programming

# class Account:
#     def __init__(self):
#         self._balance = 0   #instance variable, tied to the instance of the class
#     @property   #property is a instance variable that is read only, here i only have what's generally a getter method
#                 #no constants enforced in python, but by convention, if a variable starts with an underscore, it is considered private

#     def balance(self):
#         return self._balance
    
#     def deposit(self, n):
#         self._balance += n

#     def withdraw(self, n):
#         self._balance -= n

# def main():
#     account = Account()
#     print(f"Balance is ${account.balance}")
#     account.deposit(100)
#     account.withdraw(50)
#     print(f"Balance is ${account.balance}")

# if __name__ == "__main__":
#     main()

# MEOWS = 3 #constant by convention, constants are usually defined at the top of the file and in all caps

# for _ in range(MEOWS):
#     print('meow')

# class Cat:
#     MEOWS = 3  #class variable, shared across all instances of the class
  

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print('meow')

# cat =  Cat()
# cat.meow()

#python is not strongly typed, we can add any attribute to an instance of a class at any time
#You don't have to tell the program that you are using a str, or a float, or an int or a set


# def meow(n: int) -> str:
#     return "meow\n" * n
# number: int = int(input("Number: "))
# meows: str =  meow(number)
# print(meows, end="")


#docstrings  commenting your code
# def meow(n: int) -> str:
#     """
#     Meow n times.

#     :param n: Number of times to meow.
#     :type n: int
#     :raises TypeError: If n is not an integer.
#     :return: A string of n meows , one per line.
#     :rtype: str
#     """
#     return "meow\n" * n

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")


#argparse module 

# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="Number of times to meow" , type=int)
# args = parser.parse_args()


# for _ in range(int(args.n)):
#     print("meow")

#unpacking
# first, last = input("What's your name? ").split()

# print(f"Hello, {first} {last}")

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = [100,  50, 25]

# print(total(*coins), "knuts")    #coins is unpacking the list into individual arguments   #takes a data structure
#and unpacks it into individual arguments
#does not work for sets , works only for enumerable data structures like lists and tuples
 
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# print(total(galleons=100, sickles=50, knuts=25), "knuts")  #keyword arguments

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# #print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")  #accessing dictionary values by key
# print(total(**coins), "knuts")  #unpacking a dictionary into keyword arguments
# #** is used to unpack a dictionary into keyword arguments

#That same syntax is actually used as a visual indicator in Python
# when in a function itself might very well
# take a variable number of arguments.


# def f(*args, **kwargs):  #args is a tuple of positional arguments, kwargs is a dictionary of keyword arguments
#     print("Positional:", args)
#     print("Named:", kwargs)

# f(galleons=100, sickles=50, knuts=25)  #kwargs will capture all the keyword arguments


# def print(*objects, sep =" ", end= "\n", file=None, flush=False):  #print is a built-in function that takes a variable number of arguments
#     pass

# def main():
#     yell("This", "is", "CS50")


# def yell (*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)  #unpacking the list into individual arguments


# if __name__ == "__main__":
#     main()


# #map function   
# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.upper, words)  #map function applies the function str.upper to each element in words
#     print(*uppercased)  #unpacking the map object into individual arguments

# def main():
#     yell("This", "is", "CS50")
# def yell(*words):
#     uppercased = [word.upper() for word in words]  #list comprehension
#     print(*uppercased)  #unpacking the list into individual arguments

# if __name__ == "__main__":
#     main()

#filter without python's built-in filter function
# students = [
#     {"name": "Hermione", "home": "Gryffindor"},
#     {"name": "Harry", "home": "Gryffindor"},
#     {"name": "Ron", "home": "Gryffindor"},
#     {"name": "Draco", "home": "Slytherin"},
# ]

# gryffindor = [student["name"] for student in students if student["home"] == "Gryffindor"]


# for gryff in gryffindor:
#     print(gryff)


# students = [
#     {"name": "Hermione", "home": "Gryffindor"},
#     {"name": "Harry", "home": "Gryffindor"},
#     {"name": "Ron", "home": "Gryffindor"},
#     {"name": "Draco", "home": "Slytherin"},
# ]

# #filter with python's built-in filter function
# def is_gryffindor(student):
#     return student["home"] == "Gryffindor"

# gryffindor = filter(is_gryffindor, students)  #filter function takes a function and an iterable and returns an iterator

# for student in sorted(gryffindor, key=lambda student: student["name"]):  #sorting the iterator returned by filter function
#     print(student["name"])


#dictionary comprehension
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "home": "Gryffindor"})

# print(gryffindors)


# students = ["Hermione", "Harry", "Ron"]
# gryffindors = [{"name": student, "home": "Gryffindor"} for student in students]  #dictionary comprehension

# print(gryffindors)



# students = ["Hermoine", "Harry", "Ron"]
# for i, student in enumerate(students):
#     print(i+1, student)

# for i in range (len(students)):
#     print(i+1, students[i])

#enumerate function
# enumerate function takes an iterable and returns an iterator that produces pairs of index and value


#generators yielding values one at a time

# def main():
#     n = int(input("What's n?: "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     for i in range(n):
#         yield f"🐑 {i + 1}"
#         # yeild generates value 1 by 1 and doesn't cause too much ram
#         #to be occupied

# if __name__ == "__main__":
#     main()

#the above function if we take 1M as number of sheeps it takes forecer
#generators function help us with this issue e.g. yeild