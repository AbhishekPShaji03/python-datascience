# # sum of digits in a number

# input = 12345
# sum = 0
# while input > 0:
#     b = input % 10
#     sum = sum + b
#     input = input // 10
# print(sum)


#reverse of a number
# num = 456
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10
# print(rev)


#factorial of a number
# num = int(input("enter a number:"))
# fact = 1
# while num > 0:
#     fact = fact * num #5*1, 4*5, 3*20, 2*60, 1*120
#     num = num - 1 #5,#4,#3,#2,#1,0
# print(fact)    



#------------------- for loop ----------------------- 

# for i in range(1,10,2): #(start, stop, step)
#     print(i)

# sum of 100 numbers
# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)

#factorial of a number

# num =int(input("enter a number:"))
# fact = 1
# for i in range(1,num + 1):
#      fact = fact * i
# print("factorial:",fact)        

#multiplication table of a number

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f'{num} x {i} ={num * i}')

#find the average and sum of n numbers
# count = int(input('enter num count:'))
# sum = 0
# for i in range(count):
#     num = int(input("enter your number:"))
#     sum = sum + num
# print(f"sum is {sum}") 
# print(f"average = {sum/count}")   


# check if a number is amstring or not
# num = int(input("enter a number:"))
# temp = num
# count = 0
# while temp > 0:
#     count += 1
#     temp = temp//10

# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** count
#     temp = temp // 10
# if sum == num:
#     print("armstrong number")
# else:
#     print("not an armstrong number")        



    # prime number 

num = int(input("enter a number:"))
count = 0
     
for i in range(1,num + 1):
    if num % i == 0:
            count += 1
if count == 2:
        print("prime number")
else:
        print("not a prime number")            
