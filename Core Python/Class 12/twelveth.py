# Exceptional Handling : Errors handle karte h

# Error :  ZeroDivisionError , ValueError , NameError ,......

# What is Exception?
# Exception is a parent where we have multiple errors like : zerodivision valueerror nameerror filenotfounderror

# try & except
# try: # in this we write our code
    # a=10
    # b=10
    # print(a+b)

    # a=b
# except: # handles the error
#     print("Some Error")

# try:
#     num=10/2
#     print(num)

#     a=b
# except ZeroDivisionError as ex:
#     print(ex)
# except Exception as ex1: # all the errors are handled by Exception.
#     print(ex1)

# try:
#     a=10
#     b=0
#     result=a/b
# except ZeroDivisionError as ex:
#     print(ex)
# except Exception as ex1:
#     print(ex1)
# else: # jab try succesfully run ho jaygaa.
#     print(result)
# finally: # this will run everytime , whenever their is success or failure.
#     print("Statement Executed")

# file=open("message.txt","r+")
# data=file.read()

# print(data)

# File handling with Exceptional Handling.
try : 
    file=open("message.txt","r+")
    data=file.read()
    
except FileNotFoundError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)
else:
    print(data)