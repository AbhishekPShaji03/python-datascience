







# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("you have an error",e)
# print("mohan")        

# try:
#     a = int(input("enter :"))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero") 
# except ValueError:
#     print("check values")
# except TypeError:
#     print("check types")   
# finally:
#     print("this will always execute")


# class myerror(Exception):
#     pass
# name = "das"
# if name == "das":
#     raise myerror("name should not be das ")
# a = 5
# del(a)
# print(a)


# file handling

# # file1 = open("data.txt","r")
# # print(file1.read())
# # file1.close()

# # overwrite
# file2 = open("myfile.txt","w")
# file2.write("this month is july!!!")
# file2.close()

# file3 = open("myfile.txt","a")
# file3.write("\nhello 1")
# for i in range(1,101):
#     file3.write(f"\nabhi {i}")
# file3.close()    



# os

import os

# os.mkdir("images")
# os.remove("data.txt")
# os.rename("myfile.txt","demo.txt")
pat = "C:\\Users\ABHISHEK P SHAJI\\OneDrive\\Desktop\\python\\callmd.py"
if os.path.exists(pat):
    if os.path.exists(pat):
        print("file exixts")
    elif os.path.isdir(pat):
        print("folder exists")



