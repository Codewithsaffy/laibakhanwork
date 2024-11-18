#problem no 1
# def greatest(a,b,c):
#   if(a>b and a>c):
#     return ( "a is greatest" ,a)  
#   elif(b>a and b>c):
#     return ( "b is greatest" ,b)  
#   elif(c>a and c>b):
#     return ( "c is greatest" ,c)  
# a=int(input("Enter a number :"))
# b=int(input("Enter a number :"))
# c=int(input("Enter a number :"))
# print(greatest(a,b,c))
# #problem n0 2
# def c_to_f(f):
#   return 5*(f-32)/9
# f=int(input("Enter temperature in F:"))  
# c=c_to_f(f)
# print(f"{round(c,2)} °c")
# #problem no 3
# print("a")
# print("b")
# print("c",end="")
# print("d", end="")
# #problem no 4
# def sum (n):
#   if(n==1):
#     return 1
#   return sum(n-1)+n
# print(sum(5))    
# #problem no 5
# def pattern(n):
#   if(n==0):
#     return
#   print("*"*n)
#   pattern(n-1)
# pattern(5)    
# #problem no 6
# def inch_to_cm(inch):
#   return inch*2.54
# n=int(input("Enter a number :"))
# print("The number in cm is",inch_to_cm(n))
# #problem no 7
# def rem(l, word):
#   n=[]
#   for item in l:
#     if not(item == word):
#       n.append(item.strip(word))
#     return n

# l=["Areeba" , "Yousuf" , "Younus"]
# print(rem(l,"a"))    
#problem no 8
def multiply(n):
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
multiply(5)  