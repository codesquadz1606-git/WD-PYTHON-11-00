# String
# String is set of characters in "" is known as string.It is immutable(non-changeable). String is accessed by zero based indexing

# name="Ayush Kumar"
# print(type(name))

# name="Umesh" # we can change value by re-assigning
# print(name)

# Zero based Indexing : 0 sa start & end at len-1 , indexing is use in var_name[index number]

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# i=0
# while(i<len(name)):
#     print(f"Index {i} : {name[i]}")
#     i+=1

# name[0]="I" # not allowed in string to change any character in a string
# print(name[0])

# String Methods
name="Ankit Singh"

# startsWith
# print(name.startswith("a")) # it identitfy that name is starting with particular string or not.

# endsWith
# print(name.endswith("h"))

# lower
# print(name.lower()) # convert string to lowercase

# upper
# print(name.upper()) # convert string to uppercase

# title
# print("hello everyone".title())

# swapcase()
# print("PytHoN".swapcase())

# strip
# print("    Python    ".strip())
# print("    Python    ".lstrip(),end="")
# print("hello")
# print("    Python    ".rstrip())

# replace
# print("Ayush Kumar".replace("Kumar","Srivastava"))

# find()
# print("Srivastava".find("a")) # first occurence index.

# count
# print("Srivastava".count("a")) 

# split() : split an string into list on behalf of any object
# print("101-Ayush-Noida".split("-"))

# join()
# info=['101', 'Ayush', 'Noida']
# n=""
# print(n.join(info))

# List is a collection of multiple data of diffrent data types. List is stored in [].

# data=["Ayush",23,98.65,True]
# print(data)
# print(type(data))

# List is mutable (changeable), and it is also accessed by zero based indexing.

# data[0]="Ansh"
# print(data)

# list of list

data1=[
    ["Ansh","Noida",22],
    ["Sahil","Banaras",24]
]

print(data1[1][1])