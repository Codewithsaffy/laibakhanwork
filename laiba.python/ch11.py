# #inheritance
# class Emplyee:
#   company="Google"
#   def show(self):
#     print(f"The name of the emplyee is {self.name}")
# class programmer(Emplyee):
#   company="microscoft"
#   def showpro(self):  
#     print(f"The name of the emplyee is {self.name}")
# a=Emplyee()
# b=programmer()  
# print(a.company,b.company)  
#multiple inheritance
# class Employee:
#   company="Google"
#   def show(self):
#     print(f"The company of the emplyee is {self.company}")
# class coder:
#   language= "python"
#   def show_language(self):
#     print(f"The language of the coder is {self.language}") 

# class programmer(Employee,coder):
#   company="microscoft"
#   def showpro(self):  
#     print(f"The company of the emplyee is {self.company}")

# a=Employee()
# b=programmer()  

# b.show()
# b.show_language()
# b.showpro()
# #multilevel inheritance
# #is me parents to child 1 .child 1 to child 2
# class Emplyee:
#   company="Google"
#   def show(self):
#     print(f"The company of the emplyee is {self.company}")
# class coder(Employee):
#   language= "python"
#   def show_language(self):
#     print(f"The language of the coder is {self.language}") 

# class programmer(coder):
#   company="microscoft"
#   def showpro(self):  
#     print(f"The company of the emplyee is {self.company}")

# a=Emplyee()
# b=programmer()  

# b.show()
# b.show_language()
#super class
class Employee:
  def __init__(self):
    print("Good morning")
  a=2
class coder(Employee):
  def __init__(self):
    print("Good morning")
  b=2
class programmer(coder):
  def __init__(self):
    super().__init__()
    print("Good morning")
  c=6

# o=Employee()
# print(o.a)
# o=coder()
# print(o.a,o.b)
o=programmer()
print(o.a,o.b,o.c)

#class method 
class Employee:
  a=1
  @classmethod
  def show(cls):
    print(f"The value of class attributes is a {cls.a}")
e=Employee()
e.a=3
e.show()
#property method 
class Employee:
  a=1
  @classmethod
  def show(cls):
    print(f"The value of class attributes is a {cls.a}")
  @property
  def name (self):
    return f"{self.fname} {self.lname}"  
  @name.setter
  def name(self,name):
    self.fname=name.split(" ")[0]
    self.lname=name.split(" ")[1]  
e=Employee()
e.a=3
e.name="laiba khan"
print(e.fname,e.lname)
e.show()

#operator overloading
class Number:
  def __init__(self,a):
    self.a=a
  def __add__(self,other):
    return self.a+other.a
  def __sub__(self,other):
    return self.a-other.a
  def __mul__(self,other):
    return self.a*other.a
  def __truediv__(self,other):
    return self.a/other.a
  def __floordiv__(self,other):
    return self.a//other.a
a=Number (1) 
b=Number (2) 
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)










