## nested loop

# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             print(i,j,k)
  

#pattern
# for i in range(1,6):
#     for j in range(1,1+i):
#         print("*",end = "")
#     print()    


# reverse
# for i in range(5,0,-1):
#     for j in range(i): 
#         print("*",end = "")
#     print()    


# equilateral triangle

# for i in range(1,6):
#     for j in range(6 - i):
#         print(" ",end="")
#     for k in range(1,i+1) :   
#         print("* ",end ="")
#     print()    


# chess board
# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j)%2 == 0:
#             print("w ",end ="")
#         else:
#             print("b ",end ="")
#     print()



#H,I

# for i in range(7):
#     for j in range(5):
#         if i == 0 or i == 6 or j == 2:
#             print("*",end ="")
#         else:
#             print(" ",end ="")
#     print()
         

# for i in range(7):
#     for j in range(5):
#         if j == 0 or j == 4 or i == 3:
#             print("*",end ="")
#         else:
#             print(" ",end ="")
#     print()
         

# a = [11,13,14,15,16,17,18,19,20,12,15]
# mid = len(a)//2
# b = []
# c = []
# for i in range(len(a)):
#     if i < mid:
#         b.append(a[i])
#     else:
#         c.append(a[i])    
    
# print(b)
# print(c)


# a = [11,1,100,-900,10,15,16]
# print largest and smallest int from this list

a = [11,1,100,-900,10,15,16]
# b = max(a)
# c = min(a)
# print (b)
# print(c)

largest = 0
smallest = 0

for i in a:
    if i  > largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest,smallest)            