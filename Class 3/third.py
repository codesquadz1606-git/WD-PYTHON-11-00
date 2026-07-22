# print("Hello this is third class",end=" ")
# # ctrl +/ for comment
# print("Operators")

# variable is a container
# a=10 # this is variable
# print(a) 

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))

# print(a+b)

# num=str(20)
# print(type(num))

# num1=int(input("Enter num 1 : "))
# num2=int(input("Enter num 2 : "))
# num3=int(input("Enter num 3 : "))

# Arthemetic
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2) # qoutient : float
# print(num1%num2) # Remainder
# print(num1**num2)

# Assignment
# a=10 # valid
# 10=b # invalid

# +=, -= , *= , /= , %= , **=
# a=10;
# a+=5 # a = a+5
# print(a)
# a-=10
# print(a)
# a*=3
# print(a)
# a/=5
# print(a) # float
# a%=3
# print(a)
# a**=2
# print(a)

# Relational Operator
# print(num1<num2)
# print(num1>num2)
# print(num1>=num2)
# print(num1<=num2)
# print(num1==num2)
# print(num1!=num2)

# Logical Operator
# and : All the condition must be true , then only result will be true. If any single condition is false , result will be false.
# print(num1<num2 and num2>num3)

# or : Here any single condition is true , result will be true.
# print(num1<num2 or num2>num3)

# not : reverse the decision
# print(not(num1<num2 or num2>num3))

# name="Ayush"
# n="B"
# result=n not in name
# print(result) # Kyaa A exist kartaa h name mae.

a=[1,2]
b=[1,2]
c=a # c & a is on the same address pa h.

# They both are on diffrent address

print(a==b) # value compare
print(a is b) # address compare 
print(a is not b)

print(a is c)