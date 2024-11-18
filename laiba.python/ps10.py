# #problem no 1
# class programmer:
#   company="Microsoft"
#   def __init__(self,name,salary,pin):
#     self.name=name
#     self.salary=salary
#     self.pin=pin
# p=programmer("Laiba",12000,1234)
# print(p.name,p.salary,p.pin,p.company)
# a=programmer("areeba",10000,8734)
# print(a.name,a.salary,a.pin,a.company)
# #problem no 2
# class calculator:
#   def __init__(self,n):
#     self.n=n
#   def square(self):
#     print(f"the square is {self.n**2}")  
#   def cube(self):
#     print(f"the square is {self.n**3}")  
#   def squareroot(self):
#     print(f"the square is {self.n**1/2}")  
# a=calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# #problem no 3
# class demo:
#   a=4
# o=demo()  
# a.o=0
# print(a.o)  
# print(demo.a)

# #class attributes can't be changed


# #problem no 4
# class calculator:
#   def __init__(self,n):
#     self.n=n
#   def square(self):
#     print(f"the square is {self.n**2}")  
#   @staticmethod
#   def hello():
#     print("hello")

# a=calculator(4)
# a.hello()
# a.square()

#problem no 5
from random import randint  
class train:
  def __init__(self,train_no):
    self.train_no=train_no

  def book(self,fro,to):
    print(f"the book is from {fro} to {to}")

  def getstatus(self):  
    print(f"train no{self.train_no}")

  def getfear(self,fro,to):
    print(f"The train_no is {self.train_no} the book is from {fro} to {to}is  {randint(200,300)}")

t=train(1234)   
t.book("karachi","Lahore")
t.getstatus()
t.getfear("karachi","Lahore")

#problem no 6
# self ko change karne se kuch ho ga nahi ho ga us ki jaga kuch bhi likh sakte hai .likin readability kum ho gati hai




