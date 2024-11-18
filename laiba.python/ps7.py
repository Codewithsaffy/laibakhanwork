# #problem no 1
# n=int(input("Enter a number :"))
# for i in range(1,11):
#   print(f"{n}x{i}={n*i}")
# #problem no 2
# l=["laiba","areeba","ayesha","abrish"]   
# for name in l:
#   if(name.startswith("a")):
#     print(f"hellow {name}")
# # #problem no 3

# n=int(input("Enter a number :"))
# i=1
# while i in range(1,11):
#   print(f"{n}x{i}={n*i}")
#   i+=1
# #problem no 4
# n=int(input("Enter a number :"))
# for i in range(2,n):
#   if(n%i==0):
#     print("number is not prime")  
#     break  
# else:
#   print("number is prime")
#problem no 5
# n=int(input("Enter a number :"))   
# i=1
# sum=0
# while(i<=3):
#   sum +=i
#   i+=1

# print(sum)
# #problem no 6
# n=int(input("Enter a number :"))
# product=1
# for i in range (1, 3+1):
#   product=product*i

# print(f"the factorial of {n} is {product}")

# #problem no 7
# n=int(input("Enter a number : "))

# for i in range(1, (n+1)):
#   print(" "* (n-i), end="")
#   print("*"* (2*i-1), end="")
#   print("")
# #problem no 8
# n=int(input("Enter a number : "))

# for i in range(1, (n+1)):

#   print("*"* i, end="")
#   print("")
#problem no 9
#problem no 7
# n=int(input("Enter a number : "))

# for i in range(1, (n+1)):
#   if(i==1 or i==n):
#     print("*"*n,end="")
#   else:  
#     print("*",end="")
#     print(" "* (n-2), end="")
#     print("*",end="")
#   print("")
#problem no 10
n=int(input("Enter a number :"))
for i in range(1,11):

  print(f"{n}x{11-i}={n*(11-i)}")

