# while loop
# i = 1
# while i < 6:
#     print(i)
#     i = i + 1
# print("mohan")    

#sum of first 10 numbers
# i = 1
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)

# sum of even numbers of first 100 numbers
# i = 2
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 2
# print(sum)    

# # sum of odd numbers of first 100 numbers
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 2
# print(sum)



i = 1
esum = 0
osum = 0
while i <= 100:
    if i % 2 == 0:
        esum = esum + i
    else:
        osum = osum + i
    i = i + 1
print(esum)
print(osum)        