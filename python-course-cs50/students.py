# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

#lambda function is an anonymous function, we dont need to give it a name, if we only need to call it once 
#lambda function is defined as lambda student: student["name"]  , where student is the argument and student["name"] is the return value

##csv library 
##program for reading a CSV
# import csv

# students = []

# # Open the CSV file
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     # Read each row of the CSV file
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})  # Use "home" for the key

# # Sort the students by name and print them
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

##Program for writing a csv file
# import csv

# name = input("What's your name? ")
# home =  input("Where's your home? ")

# with open("students.csv", "a", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})


