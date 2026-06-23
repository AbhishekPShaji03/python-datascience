#----- set-----
# collection of data
# unordered
# unindexed

# contains no duplicates
# a = {1,2,3}
# b = {3,2,1}
# print(a==b)

# a = {1,2,3,4,5,3,4,2,7,8,9,6}
# # b = set
# # b = {3,2,1,4}
# print(a)

# fruits = {"mango","orange","apple","banana","watermelon"}
# for i in fruits:
#     print(i)

# union 
# intersection 
# difference

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(a.union(b))
# print(a|b)

# print(a.intersection(b))
# print(a&b)

# print(a-b)
# print(b-a)

#------dictionary-------
#key value paired datatype
# key : "value"
# userdata ={"name":"mohan","age":"27","location":"kochi","ph.no":4568878789}
# no Index
# print(userdata["age"])
# print(userdata["location"])
# mutable

# data = {}
# data["name"] = "das"
# data["age"] = 29
# data["email"] = "das@123.com"
# data["phone"] = 2762671870
# data["name"] ="priya"
# print(data)

## a=- {1,2,3,4}

# data = {'name': 'priya', 'age': 29, 'email': 'das@123.com', 'phone': 2762671870 ,'name':'das'}
# print(data)


# restrictions

# 1. keys are unique
# 2. keys are immutable type
# b= [1,2,3]
# a = {1:"hello",2:"bye",b:"ok"}
# print(a)

# -----inbuild functions-----

a = {"name":"mohan","age":30,"location":"kochi"}
# print(a.get("name"))
# print(a['location'])
# print(a.keys()) #collection of keys
# print(a.values())
# print(a.items())
# a.update({'phone':6535418658})
# a['age'] = 50
# a.pop("name")
# a.popitem()
# a.clear()
# print(a)

# for i in a:
#     print(i,a[i])

# for i,j in a.items():
#     print(i,j)    




a = "hello my name is kumar"
word = (" ")
b = []

for i in a:
    if i != " ":
        word = word + i
    else:    
         b.append(word)
         word = " "

b.append(word)
print(b) 

#above all is under one fn split

a = "hello my name is kumar"
b = a.split('a')
print(b)