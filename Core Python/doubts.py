# Questions : 3 , 9 , 4 , 

# Question 3 : Convert Celsius to Farenheit
# celsius = int(input("Enter the Celsius : "))
# convert_to_far=(celsius*9/5)+32 
# print(f"Temperature {celsius} celsius to {convert_to_far} farenheit")

# Question 4 : Swap two numbers without third variable.
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))

# print(f"Before Swapping A:{a} & B:{b}")

# a,b=b,a # I am assigning them a new value 
# print(f"After Swapping A:{a} & B:{b}")

# Question 9 : Reverse three digit number.
# n=int(input("Enter three-digit number : ")) # 123
# rev=0
# while(n>0): # 123>0(true) 12>0(true) 1>0(true) 0>0(false : loop end)
#     rev=rev*10+n%10 # 0+3=3 30+2=32 320+1=321
#     n=n//10 # 12 1 0

# print(f"Reversed : {rev}")

# Question : 18 , 17 , 13 , 14 , 15

# Question 13: Grades from Marks.
# marks=int(input("Enter the marks :"))
# >=90 : A+
# 80 to 90 : A
# 65 to 80 : B
# 55 to 65 : C
# 50 to 55 : D
# 33 to 50 : E
# <33 : F

# if(marks>=90):
#     print("Grade : A+")
# elif(marks>=80 and marks<90):
#     print("Grade : A")
# elif(marks>=65 and marks<80):
#     print("Grade : B")
# elif(marks>=55 and marks<65):
#     print("Grade : C")
# elif(marks>=50 and marks<55):
#     print("Grade : D")
# elif(marks>=33 and marks<50):
#     print("Grade : E")
# else:
#     print("Grade : F")

# Question 14: Leap Year
# year=int(input("Enter the year : "))
# if(year%4==0 or year%400==0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")

# Question 15: Check whether character is vowel or not.

# ch=input("Enter the single character : ").lower()
# if ch in 'aeiou':
#     print("Vowel")
# else:
#     print("Constant")

# Question 18 : valid Traingle
side1=int(input("Enter side 1 : "))
side2=int(input("Enter side 2 : "))
side3=int(input("Enter side 3 : "))

# sum of two sides is greater than of remanining side then it is a traingle
if (side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("Valid Triangle")
else :
    print("Not a Valid Triangle")