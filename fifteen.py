# ----------functions---------
# block of code which is executed when it is called
# to call a fn =functon_name()
# to define a fn = def function_name
# def functionname(<arguments>):
# code to be executed
# DRY - don't repeat ypurself


# def hello():
#     print("hello good afternoon!!!!!")
# hello()  #calling a function  


# arguments
# parameters

# def add2(a,b):
#     print(a+b)
# add2(1,2)
# add2(10,20)    


# types of arguments
# positional arguments

# def add2(a,b):
#     print(a+b)
# add2(1,2)    


# keyword arguments

# def fullname(fname,mname,lname):
#     print(fname+' '+mname+' '+lname)
# fullname(lname="shaji",mname="P",fname="Abhishek")    

# default arguments
# def add2(a=0,b=0):
#     print(a+b)
# add2(1,2)    


# return statement
# scope

# def add2(a,b):
#     return 1,"mohan",True
# # add2(a,b) == a+b
# # add2(4,5) == "hari"
# print(add2(1,4))


# calculator

# # n = int(input("enter a number:"))
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def main():
#     while True:
#         print("Welcome to simple calculator!!!!!!!")
#         ch = int(input("enter your choice:\n1.add\n2.sub\n3.mul\n4.div\n5.exit\n:----"))
#         x = int(input("enter number:"))
#         y = int(input("enter number:"))
#         if ch == 1:
#             print(add(x,y))
#         elif ch == 2:
#             print(sub(x,y))   
#         elif ch == 3:
#             print(mul(x,y))    
#         elif ch == 4:
#             print(div(x,y))
#         elif ch == 5:
#             break
#         else:
#             print("invalid choice")  
# main()                               



# lambda function : argument

# z = lambda x,y : x+y
# print(z(2,3))

# product of 3 number 
# square of a number

# m = lambda x,y,z : x+y+z
# print(m(2,3,5))


# z = lambda x: x**2
# print(z(3))

# perimeter of a circle

z = lambda r : 2* 3.14 * r
print(z(2))

#area of triangle

z = lambda x,y : 1/2*x*y
print(z(2,3))

#average of 5 numbers

z = lambda x,y,z,a,b : (x+y+z+a+b)/5
print(z(2,3,4,5,6))

#sqrt of a number

sqrt = lambda x: x**0.5
print(sqrt(25))

#full name of person
fullname = lambda fname,mname,lname:fname+' '+mname+' '+lname
print("abhishejk","p","shaji")

# check if a person is eligible to vote or not

check = lambda age : "eligible" if age >= 18 else "not eligible"
print(check(21))

#pep8
#standard

# age calculator
# bmi calculator