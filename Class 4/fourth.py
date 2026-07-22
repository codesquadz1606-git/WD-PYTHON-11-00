# num=11
# if(num>10): # true hotii h
#     print("Number is Greater than 10")
# else:
#     print("Number is Less than 10")

# age=int(input("Enter the age:"))
# if(age>=19):
#     print("Eligible")
# elif(age>=13 and age<=18): # it means additional statement.
#     print(f"Eligible in {19-age} years")
# else:
#     print("Not ELigible")

# Nested If else
# I Have three numbers a , b & c among all three numbers I want to find the greatest.

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))

# Method 1: Normal Solution
# if(a>b and a>c):
#     print(f"{a} is greater than {b} & {c}")
# elif(b>c):
#     print(f"{b} is greater than {a} & {c}")
# else:
#     print(f"{c} is greater than {a} & {b}")

# Method 2 : Nested Solution

# if(a>b): # a smaller
#     if(a>c):
#         print(f"{a} is greater than {b} & {c}")
#     else:
#         print(f"1.{c} is greater than {a} & {b}")
# elif(b>c): # b smaller
#     print(f"{b} is greater than {a} & {c}")
# else:
#     print(f"2.{c} is greater than {a} & {b}")

# While Loop :
# start
# while(stop):
    # code
    # step

# i=1 # start i=1
# while(i<=10): # stop 1<=10 2<=10 3<=10 ... 10<=10 11<=10(false)
#     print(i) # 1 2 3 .... 10
#     i+=1 # step i=2 , 3 , 4 ,.... , 11

# print("Loop ended",i)

# for loop
# name="Ayush"
# for n in name: # A Y U S H
#     print(n)
  
lists=["Ansh","Anay","Sidhhart","Umesh"]
for name in lists:
    print(name)
    for n in name:
        print(n)