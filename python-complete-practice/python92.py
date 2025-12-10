import python91     #import the file python91.py
#importing specific class from python91.py
from python91 import NotPrivate

test = NotPrivate("tim")  #create an object of NotPrivate class
test.display()  #call the public method display()