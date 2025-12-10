# #Filter function in Python


# # def add7(x):
# #     return x + 7   # function that adds 7 to the input x
# # def isOdd(x):
# #     return x % 2 != 0 # returns True if x is odd

# # a= [1,2,3,4,5,6,7,8,9,10]

# # b = list(filter(isOdd, a)) # filter function applies isOdd to each element in a and returns only those for which isOdd returns True


# # c = list(map(add7, filter(isOdd, a))) # map function applies add7 to each element in b
# # print(c)  # Output the final list



# # #lambda function in Python

# # def func(x):   #function that adds 5 to the input x
# #     func2 = lambda x: x + 5
# #     return func2(x)  +  85 
# # print(func(2))

# # #the above function can be written using lambda function as below as its very simple function

# # # print(func2(2))

# #lambda function with multiple parameters


# # def func(x):
# #     func2 =  lambda x: x+5
# #     return func2(x) + 85

# # func3 = lambda x, y=4: x + y  # lambda function that multiplies two inputs x and y # with default value of y as 4
# # print(func3(5)) # calling func3 with only one argument, y takes default value 4

# # print(func(2))



# # # # lambda function with map and filter functions
# # a = [1,2,3,4,5,6,7,8,9,10]

# # # newList = list(map(lambda x: x+5, a)) # map function applies the lambda function to each element in a
# # # print(newList)

# # # filter function with lambda
# # newList2 = list(filter(lambda x: x % 2 == 0, a)) # filter function applies the lambda function to each element in a
# # print(newList2)




# # #collections module in Python and counter 
# # import collections
# # from collections import Counter

# # #Containers examples are list, tuple, set, dictionary, namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict
# # #first thing is we gotta import collections module, followed by importing the specific container we want to use
# # #no error if a key is not found in Counter, it returns 0, unlike dictionary which raises KeyError
# # #1) Counter 
# # # c = Counter('gallad')  # create an empty Counter object
# # # print(c)
# # # c = Counter(['a', 'c', 'b', 'c', 'c'])  # create a Counter object from a list
# # # print(c)
# # # e = Counter({'a': 1, 'b': 2})  # create a Counter object from a dictionary
# # # print(c)
# # # d = Counter(cats=4, dogs=7)  # create a Counter object using keyword arguments
# # # # print(c)
# # # # print(c['pets'])  # access the count of 'cats'
# # # # print(list(c.elements()))  # convert the iterator to a list
# # # print(c.most_common(2)) # return all elements in the counter, sorted from most common to least common

# # # c = Counter(a=4, b=2, c=0, d=-2)
# # # d = ['a', 'b', 'b', 'c'] 
# # # c.subtract(d)  # subtract elements in d from counts in c
# # # print(c)  # Output: Counter({'a': 3, 'b': 0, 'c': 0, 'd': -2})
# # # c.update(d)  # add elements in d to counts in c , similar to subtract but adds instead of subtracts
# # # print(c)  # Output: Counter({'a': 4, 'b': 2, 'c': 1, 'd': -2})

# # # c.clear()  # remove all elements from c
# # # print(c)  # Output: Counter()
# # #we can also do arithmetic operations on Counter objects like addition, subtraction, intersection and union
# # #If the element count is less than or equal to zero, it is removed from the result in addition and subtraction operations.
# # c = Counter(a=4, b=2, c=0, d=-2)
# # d = Counter(['a', 'b', 'b', 'c'])
# # print(c + d)
# # print(c - d)
# # print(c & d)
# # print(c | d)

# # # Named Tuple in Python
# # from collections import namedtuple
# # #namedtuple is a factory function for creating tuple subclasses with named fields
# # # difference between namedtuple and tuple is that namedtuple allows us to access the elements by name instead of index

# # # Point = namedtuple('Point', 'x y z')  # create a namedtuple class called Point with fields x, y, and z
 
# # # newP = Point(1, 2, 3)  # create an instance of Point
# # # print(newP)  # access the fields by name


# # # Point =  namedtuple('Point', ['x', 'y', 'z'])  # create a namedtuple class called Point with fields x, y, and z
# # # newP = Point(1, 2, 3)  # create an instance of Point
# # # print(newP)  # access the fields by name


# # Point =  namedtuple('Point', {'x':0 , 'y':0, 'z':0})  # create a namedtuple class called Point with fields x, y, and z
# # newP = Point(3, 4 ,5 )  # create an instance of Point
# # print(newP)  # access the fields by name
# # print(newP.x, newP.y, newP.z)  # access the fields by name
# # print(newP[0])  # access the fields by index
# # print(newP._asdict())  # convert the namedtuple to a dictionary
# # print(newP._fields)  # get the field names of the namedtuple
# # # replace the value of y with 6, #actually doesn't modify the original namedtuple, it returns a new namedtuple with the modified value
# # #we need to assisgn it to a new variable
# # newP =newP._replace(y=6)  
# # print(newP)  # access the fields by name


# # p2 = Point._make(['a', 'b', 'c'])  # create a namedtuple instance from an iterable
# # print(p2)  # access the fields by name


# #colllections deque in Python , pronounced  as "deck"
# import collections
# from collections import deque

# # deque is a double-ended queue that allows us to add or remove elements from both ends with O(1) time complexity
# # d = deque()  # create an empty deque   , # by default deque has no maximum length , # we can set a maximum length by passing maxlen parameter

# # d= deque("hello")
# # print(d)

# # d.append('y')  # add an element to the right end
# # print(d)
# # d.append(5)
# # print(d)

# # d.appendleft('X')  # add an element to the left end
# # print(d)
# # d.pop()  # remove and return an element from the right end or pass an index to remove element at that index
# # d.popleft() # remove and return an element from the left end
# # print(d)

# # d.clear()  # remove all elements from the deque
# # print(d)  # Output: deque([])

# # d.extend('456')  # add multiple elements to the right end
# # print(d)
# # d.extend('hello')  # add multiple elements to the right end
# # print(d)
# # d.extendleft('123')  # add multiple elements to the left end
# # print(d)  # note that the order of elements is reversed when adding to the left end



# # d.rotate(-1)
# # print(d)  # rotate the deque to the right by 1 position, what it does is it takes the last element and moves it to the front


# d = deque("hello", maxlen=5)  # create a deque with maximum length of 5
# #we can only access the maximum length of deque, we cannot change it after creation
# #e.g. we can access by
# print(d.maxlen)
# print(d)
# d.append('y')  # add an element to the right end, since the maximum length is 5, the leftmost element 'h' will be removed
# print(d)
# d.extend([1,2,3])  # add multiple elements to the right end, since the maximum length is 5, the leftmost elements will be removed
# print(d)