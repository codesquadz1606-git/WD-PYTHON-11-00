# for i in range(10):
#     print(i)

# for i in range(0,20,2):
#     print(i)

# for no in range(10):
#     print(no)

# for i in range(1,11,1):
#     if(i==4):
#         break # loop sa bahar le aata h
#     print(i)


# for i in range(1,11,1):
#     if(i==4):
#         continue # loop ka andar element ko skip.
#     print(i)

# for i in range(1,11,1):
#     if(i==5):
#         pass # for future logic building
#     print(i)

# Right Half Pyramid
# *
# **
# ***
# ****
# *****
# row:5 , col:5
# for row in range(1,6):     # row=1,2,3,4,5
#     for star in range(row): # 0,1 0,2 0,3 0,4 0,5
#         print("*",end="")
#     print() # for new row.

# Left Half Pyramid
#     *
#    **
#   ***
#  ****
# *****
# row:5 col:5 space:5

# for row in range(1,6): # row=1,2,3,4,5
#     for space in range(row,5): # 1,5(4) 2,5(3) 3,5(2) 4,5(1) 5,5(0)
#         print(" ",end="")
#     for star in range(row):
#         print("*",end="")
#     print()

# Triangle star Pattern
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# for row in range(1,6): # row=1,2,3,4,5
#     for space in range(row,5): # 1,5(4) 2,5(3) 3,5(2) 4,5(1) 5,5(0)
#         print(" ",end="")
#     for star in range(row):
#         print("* ",end="")
#     print()

# Star Hollow Pattern
# * * * * *
# *       *
# *       *
# *       *
# *       *
# * * * * *
# row:6

for row in range(1,7): # row=1,2,3,4,5,6
    for col in range(6): # col:0,1,2,3,4,5
        if(row==1 or row==6 or col==0 or col==5):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
