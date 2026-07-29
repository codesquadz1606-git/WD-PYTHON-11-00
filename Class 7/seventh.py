# Slicing in List : [start:end-1 : -1(reverse)]
items=[True,"Baseball","Bat",23,89.67,True]
# print(items)

# print(items[0:4]) # 0 sa start ho aur 4-1 pa jaake rukke.
# print(items[-3:-1])
# print(items[2:])

# print(items[::3]) # [start:stop-1:step]
# print(items[::-1])

# print(items)
# print(items[-3:-1])

# List Methods
# append() : Add at the last of the list , single element is only added at a time.
# items.append(34)

# extend() : We can add multiple values.
# items.extend([20,30,40])

# pop() : It by defaukt removes the last element
# items.pop(0)

# items1=items # It have copied items to items1 , here elements & their address is copied.
# items1=items.copy() # copying elemnts without any previous refernces.
# items1[0]="Cricket"
# print("Items:",items)
# print("Items1:",items1)

# print(items.count(True))

# items.clear()
# print(items)

# items.reverse()
# print(items)

# nums=[12,3,45,100,20,11,55]
# # nums.sort() # for ascending to descending
# nums.sort(reverse=True) # for descending to ascending 
# print(nums)

# What is Tuple?
# Tuple also stores multiple data of diffrent data types, Tuples are immutables(non-changeable) , Tuples are also asccesd by zero based indexing.

element=(10,20,30,10,40,50,60,10)
# print(element)
# print(type(element))

# element[2]=100 # it is not valid as it is immutable object.
# print(element[2])

# Negative Indexing
# print(element[-2])

# Slicing in Tuple
# print(element[0:4])
# print(element[::-1])
# print(element[-4:-1]) # [-4:-2]

# info=(10,)
# print(info)
# print(type(info))

# Unpacking of tuple
# one,two,three,four,five,six=element
# print(one,two,three,four,five,six)

# one,*two,three=element
# print(one,two,three)

# Tuple Methods
# print(element.count(10))
# print(element.index(60))

# Built in Methods
print(len(element))
print(max(element))
print(min(element))
print(sum(element))