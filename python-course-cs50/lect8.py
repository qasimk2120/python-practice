# name = input("What is your name? ")

# file = open("names.txt", "a") #open function takes first argument as the file name, and then second argument as w for write mode
# #a means to append
# ##w is dangerous recreates the file deletes old contents
# #creates the file for me  ##open returns a file handle

# file.write(f"{name}\n") #write function writes the name to the file
# file.close() #close function closes the file but not to be used like this as there is another pythonic way and better way

##pythonic way is to use with keyword -automatically close and open the file
# name = input("What is your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
##we now want to read the file

# with open("names.txt", "r") as file:
#     lines = file.readlines() #readlines function reads all the lines in the file and returns a list of strings
#     for line in lines:
#         print("hello, ", line.rstrip())
##more better way to read the file
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello, ", line.rstrip())

#another way to read the file and sort them before outputting
# names = []
# with open("names.txt") as file:  ##open without any 2nd argument is default to read mode
#     for line in file:
#         names.append(line.rstrip()) #appending to the list

# for name in sorted(names):
#     print("hello, ", name) #printing the sorted names

##another way to sort and read in a more efficient way in python to sort in a different order we can pass 1 second argument reverse=True 
# with open("names.txt") as file:
#     for line in sorted(file, reverse=True):
#         print("hello, ", line.rstrip())

##writing a function to read and update my data in the file
names = []
with open("names.txt") as file:  ##open without any 2nd argument is default to read mode
    for line in file:
        names.append(line.rstrip()) #appending to the list

for name in sorted(names):
    print("hello, ", name) #printing the sorted names