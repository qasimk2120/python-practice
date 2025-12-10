# #tup[les are immutable(cannot be changed i.e. assign, delete elements) sequences in Python, typically used to store collections of heterogeneous data.
# # They are defined by enclosing elements in parentheses ().
# # Example:
# # my_tuple = (1, "Hello", 3.14, True)
# # print(my_tuple[0])  # Accessing elements by index

# #for and while loops
# # main difference between for and while loops is that for loops are used for iterating over a sequence (like a list, tuple, dictionary, set, or string)
# # whereas while loops are used for repeated execution as long as an expression (condition) is true

# # for i in range(5):  # for loop iterating over a sequence
# #     print(i)
# # for j in range(2, 10): # for loop with start and stop
# #     print(j)

# # for k in range(10, -1, -1):  # counting down from 10 to 0
# #     print(k)
# # start, stop, step # range(start, stop, step) # step is optional  # default is 1 # stop is exclusive #the loop will run from start to stop-1 

# #using for loop to iterate over a list
# my_list = [10, 20, 30, 40, 50]
# # for item in my_list:
# #     print(item)


# #using index to iterate over a list , # useful when you need the index of each element
# # for i in range(len(my_list)):
# #     print(my_list[i])

# #enumerate function to get index and value
# # for index, value in enumerate(my_list):
# #     print(f"Index: {index}, Value: {value}")


# #while loop with break statement
# # count = 0
# # while  True:
# #     print(count)
# #     count += 1
# #     if count == 5:
# #         break  # Exit the loop when count reaches 5

# #slicde operation on lists and strings
# # Slicing allows you to extract a portion of a list or string by specifying a start index
# x =  [0,1,2,3,4,5,6,7,8,9]
# y = ['hi', 'hello', 'hey', 'greetings', 'salutations']
# s = "Hello"

# # sliced = [start::stop: step]  # syntax for slicing # start is inclusive, stop is exclusive, step is optional, default is 1 , can be negative for reverse slicing
# # [2, 4, 6] #slicing with step , # prints elements from index 2 to 7 with a step of 2,
#  # i.e., every second element, #step is the increment between each index
# print(x[2:8:2])  

#   # ['hello', 'hey', 'greetings']  # prints elements from index 1 to 3
# print(y[1:4])  
#  # 'ell' # prints characters from index 1 to 3 , # 'H' is at index 0
# print(s[1:4])  

# print(x[2::]) # From index 2 to the end # prints elements from index 2 to the end of the list
# print(y[:3])  # From the start to index 2 # prints elements from the

# print(s[4:2:-1])  # Reverse slicing from index 4 to 3 # prints characters from index 4 to 3 in reverse order end # prints elements from the start to index 2


# sliced = x[::-1]  # Reverse the entire list, # step is -1, # prints the entire list in reverse order. # step of -1 means to decrement the index by 1
# print(sliced)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # 'olleH' # Reverse the entire string


#sets in python
# SETS are unordered, mutable (changeable), unindexed collections in Python that do not allow duplicate elements.
# They are defined by enclosing elements in curly braces {} or by using the set() function. all sets care about is if something is present or not 
# x = set([1, 2, 3, 4, 4, 5])  # Duplicates will be removed
# print(x)  # Output: {1, 2, 3, 4,


# y= set()
# s = {4, 32, 2, 2, 1, 5, 5}  # Duplicates will be removed
# s.add(1)  # Adding an element
# print(1 in s)  # Checking membership, # Output: True
# s2 = {3, 32, 22, 1}
# #there are some set operations like union, intersection, difference, symmetric difference

# print(s.union(s2))  # Union of two sets 
# print(s.intersection(s2))  # Intersection of two sets
# print(s.difference(s2))  # Difference of two sets
# print(s.symmetric_difference(s2))  # Symmetric difference of two sets


#Dictionaries in python
# DICTIONARIES are unordered, mutable (changeable), indexed collections in Python that store data in key-value pairs.
# They are defined by enclosing key-value pairs in curly braces {}. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.

# x ={'key1': 'value1', 'key2': 42, 'key3': [1, 2, 3]} # Example dictionary #this is a dictionary with three key-value pairs 
# print(x['key1'])  # Accessing value by key
# x['key4'] = 'new value'  # Adding a new key-value pair

# x['key1'] = 'updated value'  # Updating an existing key-value pair
# print(x)

# print('key' in x)  # Checking if a key exists, # Output: False
# print('key2' in x)  # Output: True

# print(x.keys())   # Getting all keys
# print(x.values()) # Getting all values
# print(x.items())  # Getting all key-value pairs as tuples

# print(list(x.keys())) # Converting keys to a list 
# print(list(x.values())) # Converting values to a list
# print(list(x.items()))  # Converting items to a list of tuples

# del x['key2']  # Deleting a key-value pair
# print(x)

# for key, value in x.items():  # Iterating over key-value pairs
#     print(f"Key: {key}, Value: {value}")

# for key in x:  # Iterating over keys
#     print(f"Key: {key}, Value: {x[key]}")


#comprehensions in python
# Comprehensions provide a concise way to create lists, sets, or dictionaries in Python. 
# They consist of brackets containing an expression followed by a for clause, and can also include optional if clauses to filter items.
# List Comprehension
# x = [x for x in range(5)] # Creates a list of numbers from 0 to 4
# print(x)  # Output: [0, 1, 2, 3, 4]

# x = [x + 5 for x in range(5)] # Creates a list of numbers from 5 to 9
# print(x)  # Output: [5, 6, 7, 8, 9]

# x = [x % 5 for x in range(5)] # Creates a list of numbers from 0 to 4 using modulus operator
# print(x)  ## Output: [0, 1, 2, 3, 4]


# x =  [[0 for x in range(100)] for x in range(5)] # Creates a 2D list (5x100) initialized with zeros
# print(x)

# x = [i for i in range(100) if i % 5 == 0] # Creates a list of numbers from 0 to 99 that are multiples of 5
# print(x)  # Output: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]


# x = {i:0 for i in range(100) if i % 10 == 0} # Creates a dictionary with keys as multiples of 10 from 0 to 99 and values as 0
# print(x)  # Output: {0: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 0, 90: 0}

# x = tuple(i for i in range(100) if i % 5 == 0) # Creates a tuple of numbers from 0 to 99 that are multiples of 5
# print(x)  # Output: (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95)