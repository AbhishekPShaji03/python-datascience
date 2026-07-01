#reccursion





# # def counttozero(n): #stub
# #     print(n)
# #     if n == 0:
# #         return
# #     return counttozero(n-1)

# # counttozero(10)

# # counttozero(10) = counttozero(9) = counttozero(8) = counttozero(7) = counttozero(6) = counttozero(5) = counttozero(4) = counttozero(3) = counttozero(2) = counttozero(1) = counttozero(0)

# #10 numbers

# def sumofn(n):
#     if n == 0:
#         return 0
#     return n + sumofn(n-1) 

# print(sumofn(10)) # 10 + sumofn(9) = 10 + 9 + sumofn(8) = 10 + 9 + 8 + sumofn(7) = 10 + 9 + 8 + 7 + sumofn(6) = 10 + 9 + 8 + 7 + 6 + sumofn(5) = 10 + 9 + 8 + 7 + 6 + 5 + sumofn(4) = 10 + 9 + 8 + 7 + 6 + 5 + 4 + sumofn(3) = 10 + 9 + 8 + 7 + 6 + 5 + 4 +3+ sumofn(2) = 10+9+8+7+6+5+4+3+2+sumofn(1)=10+9+8+7+6+5+4+3+2+1=55


# # factorial of a number
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5)) 



#scope of a variable

# scope - area in which it is recognized
# name = "abhishek" #globaal variable
# def myname():
#     name = "leo"  #local variable
#     def nickname():
#         name ="yazil" #enclosing
#         print(name)
#     nickname()
# myname()        





#modules



import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)


a = 6.3
print(math.floor(a))

#random
#time
#os
