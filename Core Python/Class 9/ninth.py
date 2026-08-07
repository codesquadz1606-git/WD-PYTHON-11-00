# Zip method
# name=["Saurav","Ankit","Tushar"]
# age=[24,32,19]

# data=dict(zip(name,age))

# print(data)

# series="AB"
# numbers=[10,20,30,40]

# data=dict(zip(series,numbers))
# print(data)

# Shallow Copy & Deep Copy
# What is Shallow Copy?
# Copying the first level elements without any previous reference.

# list
# num=[1,2,3,4,5,[10,20,30]]
# newNum=num
# num[0]=100 # old mae change kara & new mae automatically change hogaya

# Shallow Copy : Only first levels are not copied on refernce , all the nested levels are copied on the reference.
# newNum=num.copy() # is baar old mae update karna ka baad new mae change nhii huaa.
# num[0]=100
# num[5][1]=200

# print("num:",num)
# print("new num:",newNum)

# Deep Copy : Here all the nested levels elements are copied without any refernce.
# import copy
# newNum=copy.deepcopy(num)
# num[0]=100
# num[5][1]=200

# print("num:",num)
# print("new num:",newNum)

# Sets : It store unique values in {}.It is mutable.It is unordered
# elements={10,20,30,40,50,10,20}
# print(elements)

# How we can create an empty set
# data={} # empty dictonary
# data=set() # empty set

# data=set([10,20,30,40,50,30,10,20])
# print(type(data))
# print(data)

# data.add("AYush") # single element add

# data.update(["Jatin","harshit"]) # multiple elements add.

# Sets are also immutable.

# fs=frozenset([10,20,30,40])
# fs.add(300)
# print(fs)

# pop() : removes random element
# data.pop()

# remove() : removes the mentioned element
# data.remove("harshit")
# data.remove("harsh") # error : keyerror

# discard()
# data.discard("harshit")
# data.discard("harsh") # do not gives the error for unknown element

# clear()
# data.clear()

# copy() : generates a copy.

# print(data)

# Mathematical Operation
# union , intersection , diffrence , symmetric_diffrence

# A={10,20,30,40}
# B={30,40,50,60}

# union : Merge all the set.
# print( A | B , A.union(B))

# Intersection : Common elements from the set
# print(A & B , A.intersection(B))

# Diffence : 
# print(B-A , A.difference(B))

# symmetric_difference : Overall Diffrence b/w the sets.
# print(A ^ B , A.symmetric_difference(B))

# Functions : It is a block of code that is used to define a particular opertion & it is executed when it is called.

# Syntax : 
# def func_name(): # declare & define a function
    # code

# func_name() # calling a function

# def greet():
#     print("hello everyone")

# greet()

# Parameter & Argument Function
# Parameter : A variable that is passed in the scope of function, which are used within the function.

# What is Return Keyword?
# It is used to transfer value to function itself.

# def sum(a,b,c):
#     print(a+b+c)
#     return a+b+c # this value is stored in function.


# # Arguments : Value that is paased in a scope of function while calling a function i.e Arguments.
# print(sum(10,20,30))

# Default Parameter.
# def info(name,age,city="Noida"):
#     print(name,age,city)

# info("Kamal",34,"Delhi")

# def fullName(fname,lname="Sharma"):
#     print(fname,lname)

# fullName("Rohit")
# fullName("Yogesh","Singh")

# def number(*num): # for tuple
#     print(num)
#     print(type(num))

# number(10,20,30,40,50,60)

# def info(**args): # for key value pair i.e dictonary.
#     print(args)

# info(name="AYush",city="Ghaziabad",pincode=201002)

# Scope of Variables
# Their are two types of scopes : 
# i. Local
# ii. Global Scope

count=10 # gloabally vallue declared.
def access():
    # count1=100 # it is defined as local scope.
    global count # now we can access as well as edit the variable
    count+=1



print(count)
access()
print(count)