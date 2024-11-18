# #walrous operators
# if (n := len([1,2,3,5,6,67])) >3 :
#   print(f"list is too long {n} elements")
# #types defination in python
# n:int =4
# #is tarike se likhne ko hum types defination in python khete hai
# #advance type hints
# from typing import List 
# n:List[int]=[1,2,3]
# #is tareke se likhne ko advance type hints khete hai
# #match case
# def n (status):
#   match status:
#     case 200:
#       return "ok"
#     case 404:
#       return "not found"
#     case _:
#       return "unknown"
# print(n(200))

# #murged dictionary
# d1={1:"a",2:"b"}
# d2={3:"c",4:"d"}
# la=d1|d2
# print(la)

# #exception
# try:
#   a=int(input("Enter a number :"))
#   print(a)
# except Exception as e:
#   print(e)  
# print("Thank you")  

# #raise exception
# a=int(input("Enter a number :"))
# b=int(input("Enter a number :"))
# if b==0:
#   raise ZeroDivisionError("b can not be zero")
# else:
#   print(a/b)
# #try else
  
# try:
#   a=int(input("Enter a number :"))
#   print(a)

# except Exception as e:
#   print(e)  

# else:
#   print("no exception")#agar try nahi ai ga to else print nahi hota

# #try finally
# try:
#   a=int(input("Enter a number :"))
#   print(a)

# except Exception as e:
#   print(e)  

# finally:
#   print("no exception")#finally chale ga hi chale ga to hum finally q laga rahe hai direct print kar de lekin gab hum function istamal kare ge to ye tab bhi print ho ga 
# def f():
#   try:
#     a=int(input("Enter a number :"))
#     print(a)
#     return

#   except Exception as e:
#     print(e) 
#     return 

#   finally: 
#     print("no exception")
# f()    
# # from ch10.py import Employee#import karne ka tareka
#global 
a=89
def f():
  global a
  a=3
  print(a)
f()  
print(a)
#enumerate
l=[1,2,3,4,5]
for index ,item in enumerate(l):
  print(f"the items number is {index} and its value is {item}")

#list compherension
l=[1,2,3,4,5]
addlist=[i+i for i in l]  
print(addlist)# add bhi ker sakte hai square bhi nikal sakte just example hi



