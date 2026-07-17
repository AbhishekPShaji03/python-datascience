# generators
# def mydata():
#     yield "one"
#     yield "two"
#     yield "three"
#     yield "four"
#     yield "five"
#     yield "six"

# a = mydata()
# print(next(a))
# print(next(a))
# print(next(a))

# b = []
# i = 0
# while True:
#     b.append(i)
#     i = i + 1

# def infiniz():
#     i = 1
#     while True:
#         yield i
#         i = i + 1

# inifine_numbers  = infiniz()
# print(inifine_numbers)
# for i in inifine_numbers:
#     print(i)
# import sys

# def crore():
#     for i in range(1,10000001):
#         yield i

# b = crore()
# # print(sys.getsizeof(a))
# print(sys.getsizeof(b))


# map
# maps each item in an itreable to a function
# map(func,itreable)


# def square(z):
#      return z**2

# products = [
#     ("nike x11",178),
#     ("apple watch",456),
#     ("samsung s24",999),
#     ("ps5",700),
#     ("iphone",1000)

# ]

# def toINR(z):
#     return z[1]*96.34

# result = filter(toINR,products)
# print(list(result))

def iseven(a):
    if a%2 == 0:
        return a
a = [1,2,3,4,5,6,7,8,9,10]

result = filter(iseven,a)
print(list(result))