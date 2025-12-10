''' Short 1:  Example of a simple class to represent a package with attributes like number, sender, receiver, and weight. 
class Package:
    def __init__(self, number, sender, receiver, weight):
        self.number= number    #these are instance variables
        self.sender = sender   # they are tied to the instance of the class
        self.receiver = receiver
        self.weight = weight

    # I create, later on, a new object, this self refers to the instance,
    # that new object, I'm creating when I were, for instance,
    # to call something like Package.
    # this particular method __init__( )  ,#one called dunder init,
    # which allows me to use my template, my class, here
    # #to later on instantiate or create some particular object from this template


#dunder str is a special method that is called when you try to print an object of the class


def main():
    packages = [
        Package(number=1, sender="Alice", receiver="Bob", weight=2.5),    #instance of the class
        Package(number=2, sender="Charlie", receiver="David", weight=1.2),  #instance of the class
        Package(3, "Eve", "Frank", 3.0)                                   #instance of the class
    ]

    # lets think of the above data as a real object, we can create a class to represent it and its properties
    # for example the package can have  some kind of identifier e.g. id, sender, receiver, weight etc




main()
'''


''' Short 2: Example of a simple class to represent a point in 2D space with methods to calculate distance from origin and move the point. '''

# class Food:
#     base_hearts = 1   #class variable, shared by all instances of the class
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.hearts = Food.calculate_hearts(ingredients)

#     @classmethod
#     def calculate_hearts(cls, ingredients):
#         # Simple heuristic: 1 heart per ingredient
#         hearts = cls.base_hearts  #accessing class variable using cls

#         for ingredient in ingredients:
#             if("hearty " in ingredient):
#                 hearts += 2
#             else:
#                 hearts += 1
#         return hearts
    
#     @classmethod
#     def from_nothing(cls, hearts):
#         food = cls(ingredients=[])
#         food.hearts = hearts
#         return food

# def main():
#     mushroom_skewer = Food(["mushroom", "hearty mushroom"])
#     print(f"This Skewer heals {mushroom_skewer.hearts} hearts.")

#     #give user a new way of creating an instance of the class
#     #maybe i want the user to find some food
#     mushroom_skewer = Food.from_nothing(hearts=5)
#     print(f"This Skewer heals {mushroom_skewer.hearts} hearts.")



# main()


# ''' Short 3: Instance Variables. '''
# class Package:
#     def __init__(self, number, sender, receiver, weight):
#         self.number= number    #these are instance variables
#         self.sender = sender   # they are tied to the instance of the class
#         self.receiver = receiver
#         self.weight = weight

# def main():
#     packages = [
#         Package(number=1, sender="Alice", receiver="Bob", weight=2.5),
#         Package(number=2, sender="Charlie", receiver="David", weight=1.2),
#         Package(3, "Eve", "Frank", 3.0)
#     ]

#     for package in packages:
#         print(f"Package {package.number} from {package.sender} to {package.receiver} weighs {package.weight} kg.")

# main()

''' Short 4: Instance Methods. '''
class Package:
    def __init__(self, number, sender, receiver, weight):
        self.number= number    #these are instance variables
        self.sender = sender   # they are tied to the instance of the class
        self.receiver = receiver
        self.weight = weight


    def __str__(self):
        return f"Package {self.number} from {self.sender} to {self.receiver} weighs {self.weight} kg."

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

#method here is a particular function that is tied to the instance of the class

def main():
    packages = [
        Package(number=1, sender="Alice", receiver="Bob", weight=5),   # this is an instance of the class
        Package(number=2, sender="Charlie", receiver="David", weight=10),
        Package(3, "Eve", "Frank", 20)
    ]

    for package in packages:
        print(f"{package} costs {package.calculate_cost(cost_per_kg=2)}" )

main()