# # # #problem no 1
# # # class twoDvector:
# # #   def __init__(self,x,y):
# # #     self.x=x
# # #     self.y=y
# # #   def show(self):
# # #     print (f"the value of twoD vector is {self.x}x + {self.y}y")
# # # class threeDvector(twoDvector):    
# # #   def __init__(self,z,x,y):
# # #     super().__init__(x,y)
# # #     self.z=z
    
# # #   def show(self):
# # #     print (f"the value of twoD vector is {self.x}x + {self.y}y+ {self.z}z")

# # # a=twoDvector(2,3)
# # # a.show()    

# # # b=threeDvector(2,4,6)
# # # b.show()    

# # #problem no 2
# # class Animals:
# #   pass
# # class pets(Animals):
# #   pass
# # class dog(pets):
# #   @staticmethod
# #   def bark():
# #     print("Bow Bow")
# # a=dog()    
# # a.bark()

# # #problem no 3
# # class Employee:
# #   salary=234
# #   increment=20
# #   @property
# #   def salaryafterincrement(self):
# #     return (self.salary + self.salary * (self.increment/100))
# #   @salaryafterincrement.setter
# #   def salaryafterincrement(self,salary):  
# #     self.increment=((salary/self.salary)-1)*100

# # e=Employee()    
# # e.salaryafterincrement=280.0
# # print(e.increment)

# #problem no 4
# class complex:
#   def __init__(self,r,i):
#     self.r=r
#     self.i=i
#   def __add__(self,a):  
#     return complex(self.r+a.r,self.i+a.i)
#   def __mul__(self,a):  
#     real_part = self.r * a.r - self.i * a.i
#     imag_part = self.r * a.i + self.i * a.r
#     return complex(real_part, imag_part)
#   def __str__(self):
#     return f"{self.r}r + {self.i}i"  
# c1=complex(2,3)
# c2=complex(4,5)
# print(c1+c2)    
# print(c1*c2)
#problem no 5
class vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def __add__(self,a):
    result=vector(self.x+a.x,self.y+a.y,self.z+a.z)
    return result  
  def __mul__(self,a):
    result=(self.x * a.x + self.y * a.y + self.z * a.z)
    return result  
  def __str__(self):
    return f"{self.x} , {self.y} , {self.z}"
v1=vector(2,3,4)
v2=vector(4,5,6)
v3=vector(6,7,8)
print(v1+v2)    
print(v1*v3)    

print(v1*v2)    
print(v1+v3) 


