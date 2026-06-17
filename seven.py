#logical operators
# and

# true true = true
# true false = false
# false true = false
# false false = false

a = 7
b = 10
if a > 15 and b == 10:
    print("yes")
else:
    print("no")
# or
# true true = true  
# true false = true
# false true = true
# false false = false

a = 6
b = 7
if a > 6 or b == 7:
    print("yes")

#not
a = 10
print(not a == 10)


#larger of 3 numbers
a = 10
b = 11
c = -100
if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")


# check if a number is a multiple of 3 and 5
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("true")
else:
    print("false")    