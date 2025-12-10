#types of data in python == strings, ints, floats, bools, lists, dictionaries,
#list, is just a set of miltiple values

# students = ["Hermoine", "Harry", "Ron"]
# #listing  a list of students, we cannot use _ here, as we will confuse others, here our variable here will be student to be readable
# for student in students:
#     print(student)

##########another way of solving the above problem#####
# students = ["Hermoine", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i + 1, students[i])

#####dict in python #####, multi-dimensional, associate one value with another, keys and values pair in terms of programmers
# students = ["Hermoine", "Harry", "Ron", "Draco"]
# hourses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]   #this way of using two lists doesn't works well

##declaring  dict in python #####, we use {} for dictionary, dictionaries allow us to use actual words as ur indices
# students = {
#     "Hermoine": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
#     }
# for student in students:
#     print(student ,students[student], sep=" ")

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")