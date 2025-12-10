#libraries are something that others wrote and you can use it in your own code
#library named random 
#from is a keyword in python which can be used to more specific about importing a specific function from that file
#by using just import random we bring everythign inside
#for importing a library you use the import keyword
################ Random Module in use ################

# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)

# from random import randint
# roll = randint(1, 6)
# print(roll)

# from random import shuffle

# cards = ['Jack', 'Queen', 'King', 'Ace'] #functions takes a list 

# shuffle(cards)
# for card in cards:
#     print(card)

############ Statistics Module in use ################
# import statistics
# print(statistics.mean([100,90])) #mean is the average of the numbers

################ command line arguments of programs \\ sys module ################
#argv -> a magical variable => provides a list of all words that the human typed in their prompt
#python saved the name of the file we are executing  in sys.argv 

# import sys
# #Check for errors
# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# for arg in sys.argv[1:-1]:

#     print("hello, my name is", arg)

#moving to packages , third party libraries are known as package. we can install it and gain more functionality

###################cowsay #################
# import cowsay

# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


############application programming interface, requests package########################
# import json
# import requests
# import sys


# if len(sys.argv) != 2:
#     sys.exit("Usage: python api_example.py <search_term>")

# response =  requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
# o  = response.json()
# for result in o ["results"]:
#     print(result["trackName"])

############making our own library################
import sys

from module import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])