# inheritance

# 3 types
# single level
# multi level
# multiple level

# class person1:
#     pass
# def walk(self):
#     print("person can walk")
# def smile(self):
#     print("person can smile hahahha") 

# class person2(person1):
#     pass
# def read(self):
#     print("person can read")
# def write(self):
#     print("person can write") 

# p2 = person2()
# p2.smile()



# multilevel


# class person1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def smile(self):
#         print("person can smile hahahha")
#     def speak(self):
#         print("person 1 can speak")     

# class person2:
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write") 
#     def speak(self):
#         print("person 2 can speak")    


# class person3:
#     def __init__(self):
#         pass
#     def sleep(self):
#         print("person can walk")
#     def eat(self):
#         print("person can smile hahahha") 
#     def speak(self):
#         print("person 3 can speak")

# class person4(person3,person2,person1):
#     def __init__(self):
#          pass
#     def run(self):
#         print("person can read")
#     def jump(self):
#         print("person can jump") 
#     def speak(self):
#         print("person 4 can speak")
#         super().speak()    

# p4 = person4()
# p4.jump()        


# # mro 
# method resolution order



# polymorphism


# poly - many
# morphism - forms
# operator overloading

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,otr):
#         return self.m1+self.m2,otr.m1+otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)        
# print(s1+s2)


# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __sub__(self,otr):
#         return self.m1-self.m2,otr.m1-otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)        
# print(s1-s2)

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __truediv__(self,otr):
#         return self.m1/self.m2,otr.m1/otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)        
# print(s1/s2)

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __gt__(self,otr):
#         return self.m1>self.m2,otr.m1>otr.m2

# s1 = Student(7,8)
# s2 = Student(6,10)        
# print(s1>s2)



# method overloading

# class A:
#     def __int__(self):
#         pass
#     def hello(self):
#         print(" A hello")
# class B(A):

#     def __init__(self):
#         pass
#     def hello(self):
#         print("B hello")    
# b = B()
# b.hello()    


# abstraction

# from abc import ABC,abstractmethod
# class Animal(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def make_sound(self):
#         print("animal makes sound")
# class Dog(Animal):
#     def __init__(self):
#         pass
#     def make_sound(self):
#         print("bow bow")

# d = Dog()
# d.make_sound()


# encapsulation

# access modifiers
# public 
# protected
class Student:
    def __init__(self):
        self._name = "Abi"

class Child(Student):
    def display(self):
        print(self._name)

c = Child()
c.display() 



# private
class Student:
    def __init__(self):
        self.__name = "Abi"

    def display(self):
        print(self.__name)

s = Student()
s.display()

