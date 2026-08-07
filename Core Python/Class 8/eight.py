# Dictonary : It is written inside {key : value}
info={
    "name":"Shivam",
    "age":25,
    "city":"Gurgaon",
    "pincode":122001
}

# info=dict(
#     name="Shivam",
#     age=25,
#     city="Gurgaon",
#     pincode=122001
# )

# print(info)
# print(type(info))

# Value Accessing
# Method 1: Using [keyname]
# print(info["pincode"])
# print(info["marks"]) # error 

# Method 2: Using get(keyname)
# print(info.get("name"))
# print(info.get("marks")) # None

# Adding & Updating Elements in Dictonary
# info["gender"]="Male" # koi key add bhi ho jaygaa
# info["name"]="Vishwas" # koi key update bhi ho jaygaa
# print(info)

# dict of dict : Nested Dictonary
# info1={
#     "name":"Utkarsh",
#     "skills":{
#         "skill1":"React",
#         "skill2":"Node",
#         "skill3":"Express",
#         "daSkills":{
#             "da1":"Pandas",
#             "da2":"Seaborn"
#         }
#     }
# }

# print(info1["skills"]["daSkills"]["da1"])

# dict of list
# info={
#     "name":"Shivam",
#     "age":25,
#     "city":"Gurgaon",
#     "pincode":122001,
#     "skills":["C","C++","Java","Python"]
# }

# print(info["skills"][2])

# list of dict
# datas=[
#     {
#         "name":"Shivam",
#         "city":"Delhi",
#         "gender":"Male"
#     },
#     {
#         "name":"Shivani",
#         "city":"Noida",
#         "gender":"Female"
#     },
#     {
#         "name":"Shubh",
#         "city":"Gurgaon",
#         "gender":"Male"
#     },
#     {
#         "name":"Hemant",
#         "city":"Delhi",
#         "gender":"Male"
#     }
# ]

# print(datas)

# for el in datas:
#     print(el)

# data : name , age , city : 5 data 

data=[] # empty List

for i in range(5): # 0 sa 4 ( 5 times)
    info={} # empty dictonary

    name=input("Enter the name:")
    age=input("Enter the age:")
    city=input("Enter the city:")

    info["name"]=name
    info["city"]=city
    info["age"]=age

    data.append(info)
    print(f"{i+1} user added")

print(data)

# Methods : 
# keys()
# print(info.keys())

# values()
# print(info.values())

# pop(keyname)
# info.pop("age")
# print(info)

# popitem() removes last key
# info.popitem()
# print(info)

# clear()
# info.clear()
# print(info)
