# find vowels and their position in a string

# name = input("enter your name:")

# for i in range(0,len(name)):
#     #print(i,a[i])
#     if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
#         print(i,name[i])

# create a list of even numbers and odd numbers from first 100 numbers

# num = []
# even = []
# odd = []

# for i in range(1,101):
#     num.append(i)
# for i in num :
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)            


# remove duplicates from the list

# c = [1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# b =[]
# for i in c:
#     if i not in b:
#         b.append(i)
# print(b)        

# # break continue pass

# # pass
# age = 0
# if age >= 18:
#     pass
# b = 10
# print(b)

## break
# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

## continue
# for i in range (1,11):
#     if i == 6:
#         continue
#     print(i)



#prime number hw another method

# num = int(input('enter your number:'))
# prime = True
# if num == 1:
#     prime == False
# else:
#     for i in range(2,6):
#         if num % 1 == 0:
#             print("not a prime number")
#             break
#     else:
#             print("prime number")    

# input n words and make it into a sentence

n = int(input("enter the number of words:"))

sen = " "

for i in range(n):
    word = input("enter words:")
    sen = sen + word + " "
print("sentence: ",sen)

#reverse a string without using [::-1]

str = input("enter a string:")
rev = " "
for i in range(len(str)-1,-1,-1):
    rev = rev + str[i]

print("reversed string:",rev)    
