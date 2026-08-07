# class Car(): # this is my class
#     pass

# Gwagon=Car() # object
# Gwagon.windows=4

# print(Gwagon.windows)

# Wagnor=Car() # Object 2
# Wagnor.doors=4

# # print(Wagnor.windows)
# print(Gwagon.doors)

class Dog():
    # Constructor
    def __init__(self,name,age): # this function belongs to the same class.
        self.name=name
        self.age=age

    def details(self):
        print(f"Dog name is {self.name} & age is {self.age}")

    def bark(self):
        print(f"{self.name} is barking ")

dog1=Dog("Bruno",4) # totally new object baana
dog1.details()
dog1.bark()

dog2=Dog("Tommy",2.5) # yeh bhi totally new object banaa
dog2.details()
dog2.bark()