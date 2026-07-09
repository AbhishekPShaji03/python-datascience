# object oriented programing
# object
# real life entity


# 2
# attributes - define an object
# behavior/method - functionalities of object

# class - blueprint

# methods- function inside a class

# class Car:
#     def start():
#         print("car has started")
#     def stop():    
#         print("car has stoped")
# c1 = Car
# c2 = Car   
# c3 = Car
# c3 = Car
# c2.start()
# c2.stop()



# class Bike:
#     def start():
#         print("Bike has started")
#     def stop():    
#         print("Bike has stoped")
# c1 = Bike
# c2 = Bike   
# c3 = Bike
# c3 = Bike
# c2.start()
# c2.stop()


# constructor - used to initialize an object

# class Car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#         # print("object created")
#     def start(self):
#         print(f"{self.name} has started")
#     def stop(self):
#         print("car stopped")


# c1 = Car("swift","black")
# c2 = Car("city","red")

# # c1.start()
# c2.start()






# create a class student
# with 6 attributes name ,m1,m2,m3,m4,m5

# 3 methods
# sum_of_marks()
# average of marks()
# display()

# class Student:
#     def __init__(self, n, m1, m2, m3, m4, m5):
#         self.name = n
#         self.mark1 = m1
#         self.mark2 = m2
#         self.mark3 = m3
#         self.mark4 = m4
#         self.mark5 = m5

#     def sum_of_marks(self):
#         return self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5

#     def average_of_marks(self):
#         return self.sum_of_marks() / 5

#     def display(self):
#         print(f"Student {self.name} has mark of {self.mark1},{self.mark2},{self.mark3},{self.mark4},{self.mark5} ")
#         print("Sum of Marks:", self.sum_of_marks())
#         print("Average of Marks:", self.average_of_marks())


# s1 = Student("Abhi",45, 49, 47, 39, 40)
# s1.display()