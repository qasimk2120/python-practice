########## while loop code #################
###while someething is true it keeps running, as soon as it is false it stops
# def main():
#     x = input("Animal's sound: ")
#     i = 0
#     animalSound(x,i)

# def animalSound(sound,i):
#     #while loop
#     while i < 3:
#         print(f"{sound}")
#         i += 1   #python doesn't have i++ or i-- instead it has i += 1 or i -= 1
        

# if __name__ == "__main__":
#     main()


#list is a way of containing multiple values all in the same place in the same variable  [0,1,2]
########## for loop code #################
##for allows us to loop over  a list of items
# for i in range(3): #dont manually specify the list of values, use a function someone else designed for python ##poorly designed
#     #range expects as input at least one argument,and that number is going to be the number of values you want back.
#     # Those values are going to start at 0 and go to 1, to 2, and so forth,
#     #but they will go up two but not through the number you specify.
#     print("meow") #poorly designed

    #use _ for a variable you dont care about because you are not using it later
# for _ in range(3):
#     print("meow") #well designed
    #pythonic way of repeating something 3 times
# print("meow" * 3) #pythonic way of repeating something 3 times, not a good thing as we are getting it in same line

#use a \n for a new line 
# print("meow\n" * 3, end="")

#taking a value from the user for inputs
# #A very common paradigm in Python, when you want to get user input that matches a certain expectation you have,
# that it's all positive, that it's all negative, or just something like that, you just immediately say while true.
# You deliberately, and a little dangerously but a very conventionally,induce an infinite loop.
# while True:
#     n = int(input("Positive number: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow") 

## functional programming for python loops
# def main():
#     number =  get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("Positive number: "))
#         if n > 0:
#             break
#     return n
        
# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()