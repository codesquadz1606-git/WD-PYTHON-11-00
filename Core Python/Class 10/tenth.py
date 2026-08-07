# Recursion
# It is technique where function calls itself until it reaches its base condition.

# Working with recursion we have 2 components:
# 1. base case
# 2. recursive case

# def greet(n):
#     # base case
#     if(n==0): # 5==0(false) 4==0(false) 3==0(false) 2==0(false) 1==0(false) 0==0(true : exit)
#         return 1;
#     print("Hello Everyone") # 1 2 3 4
#     greet(n-1) # recursive case , greet(4) greet(3) greet(2) greet(1) greet(0)

# greet(5)

# call 1 greet(5) greet(4) greet(3) greet(2) greet(1) greet(0)


# Sum of first n natural numbers.
# def sum(n):
#     if(n==0): # base case
#         return 0;
#     sumN=sum(n-1) # recursive call
#     sumNm=sumN+n
#     return sumNm

# print(sum(10))

# Factorial first n natural numbers
# def fact(n):
#     if(n==0):
#         return 1
    
#     # factN=fact(n-1)
#     # factNm=factN*n
#     # return factNm

#     return fact(n-1)*n

# print(fact(5))


# What is module , how to import any module & how to create any custom module.
# math
# random
# sys
# os
# string
# datetime

import math 
# print(dir(math))

# from math import sqrt,ceil,floor
# result=sqrt(41)
# print(result)
# print(floor(result))
# print(ceil(result))

# result=math.pi
# result=math.factorial(5)
# result=math.gcd(12,18)
# result=math.lcm(12,18)
# print(result)


# import random
# from random import random,randint,randrange,choice,choices

# print(dir(random))
# print(random()) # create random number b/w 0 to 1.
# print(randint(1,10))
# print(randrange(0,100,2))

# data=["Noida","gurgaon","delhi","faridabad"]
# # print(choice(data))
# print(choices(data))

# import numpy

# print(dir(numpy))

# import custom_modules.maths as mt
# result=mt.addition(2,10)

from custom_modules.maths import addition,subtract
result=subtract(10,7)
print(result)