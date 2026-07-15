# # Q)plot the points on a cartisian plane which has 2 coordinates x and y. do the following

# # 1.define a class point.its instance should have 2 attributes x and y 
# # x and y default value must be Zero

# # 2. define an instance method reset().
# #    when called it will set x,y values to zero(ie it will set the points to origin(0,0))

# # 3. d4efine an method move().
# #    this should change the method x and y.

# # 4.use this move method to update reset() method.

# # 5.  define 2 methods xmove an ymove.
# # this should move the values of x and y seperately.


# # class point:
#     # def __init__(self,x=0,y=0):
#     #     self.x = x
#     #     self.y = y

#     # def move(self,x,y):
#     #     self.x = x
#     #     self.y = y

#     # def reset(self):
#     #     self.move(0,0) 

#     # def xmove(self,x):   
#     #     self.x = x

#     # def ymove(self,y):
#     #     self.y = y

#     # # def display(self):

                

# # p1 = point(-1,10)
# # print(p1.x,p1.y)
# # p1.reset()
# # print(p1.x,p1.y)
# # p1.move(3,4)
# # print(p1.x,p1.y)



# wapython class queue that implements a basic queue data structure with the enque and deque methods.
# the enque method should add an element to the rear of the queue,and the dequeue method should remove and return the remaining element from the queue.
# additionally,include a method is empty to check if the queue is empty


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,x):
        self.queue.append(x)
        print(x,"added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            x = self.queue.pop(0)
            print(x,"remove from queue") 
            return x  
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def display(self):
        print("Queue:", self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)    
q.enqueue(30)
q.display()

q.dequeue()

q.display()

print("Is Queue Empty?", q.is_empty())


