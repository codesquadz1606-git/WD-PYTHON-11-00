# File Handling
# File handling is a process where we create , reading , write , update & delete any python file.

# open(filepath,operation)

# operation : r (read)

# file=open("text.txt","r") # object 
# print(file)

# data=file.read() # this function read the data in  object
# print(data)

# Operation : w (write)
# file=open("text.txt","w") # it oerlaps the previous data.
# file.write("I am Fine.")

# Operation : a (append)
# file=open("text.txt","a") # here we do not overlaps the data, we only add the data.
# file.write("\nThis is new line")

# r+ ( Read & write) , w+(Create & Write) , a+(Create & append)

# file=open("new.txt","r+")
# # file.write("Hello This is new File")
# data=file.read()
# print(data)
# file.close() # data leakage

# For removing any file
# import os
# os.remove("new.txt")

file=open("text.txt","r+")
# read
# file.seek(29) # this is a pointer

# readline : print all lines in list
# data=file.readlines()

# read(number)
# data=file.read(15)
# print(data)

# Pointer
# file.write("Hello")
# print(data)

# data=[
#     "python\n",
#     "pandas\n",
#     "numpy\n",
#     "seaborn"
# ]

# file.writelines(data)

data=file.readlines()
print(data[0])
