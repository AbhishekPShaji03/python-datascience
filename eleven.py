#list

#collection of data

#a = [2,3,4,5,6,7,8,9,10]
#properties

#1 . list can have any elements of any size
#data = [1,2,3,"mohan",true,[12,13,14]]

#2 . list are ordered

# a = [1,2,3,4]
#b = [3,2,1,4]

#print(a == b)

#3. lists are indexed
 
# a = [11,12,13,14,15,16,17,18,19]

# print(a)
# print(a[1])
# print(a[3:8])
# print(a[0:9:2])
# print(a[::])
# print(a[::-1])

# [start:stop:step]

# print(a[0])
#index format 0,1,2,3,4.....


#4. lists are mutable
 #but string is immutable

# a = [11,12,13,14,15]
# a[0] = 'mohan'
# print(a)

#b = "mohan"
#b[0] ="h"
#print(b)

#5. dynamic

# a = [11,12,13,14,15]
#a[0:2] =[31,32,33,34,35,36,37]
# print(a)

# a = [31,32,33,34,35,36,37,13,14,15]
# a[0:7] = ['mohan']
# print(a)

# 6. lists are nested

# a = [11,12,[100,300],14,15]

# b = a[2]
# b[0]
# print(a[2][0])


#inbuild methods

#to add elements 
# append(element)
# adds an element to the end of the list

# a = [11,12,13,14,15]
# a.append(100)
# a.append(200)
# print(a)

#extend()
#adds an itreable to the list

# a = [11,12,13,14,15]
# a.extend([23,24,"mohan"])
# print(a)


#insert(index,value)
# a = [11,12,13,14,15]
# a.insert(0,"mohan")
# print(a)


# to remove elements

#remove(element)
# pop(),pop(index)

# a = [11,12,13,14,15,16,17,18,19]
# a.remove(11)
# print(a)

#if  there is more same numbers there (eg:11,11,11) it will remove only the first occured number

# a = [ 11,12,13,14,15,16,17,28,29]
# # a.pop(0)
# a.pop()
# print(a) 


# tuple
# collection of data 
#a = (2,3,1,"mohan",672,32,2,23)
#orderd
#indexed
#immutable

# a =(1,2,3,4)
# a[0] =10
# print(a)

#2 boxes

#elastic - list 
#metal box - tuble

# itration

# a = [11,12,13,14,15]
# b = "mohan das"
# c = (100,200,300,400,500)

# for i in c:
#     print(i)

# a = "mohan"

# print(a[0])
# print(len(a))

# for i in range(0,len(a)):
#     print(i,a[i])
# fruits = ["apple","orange","banana","watermelom","pinapple","mango"]

# for i in range(0,len(fruits)):
#     print(i,fruits[i])



#prime no