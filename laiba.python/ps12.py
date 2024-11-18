# # problem no 1
# try:
#   with open ("file3.txt","r") as f:
#     print(f.read())
# except Exception as e:
#   print(e)    
# try:
#   with open ("file4.txt","r") as f:
#     print(f.read())
# except Exception as e:
#   print(e)    
# try:
#   with open ("file5.txt","r") as f:
#     print(f.read())
# except Exception as e:
#   print(e)    
#   #problem no 2
# l=[1,2,3,4,5,6,7,8,9,10]
# for i , items in enumerate (l):
#   if(i==2 or i==4 or i==6 ):
#     print(items)
# #problem no 3
# n=int(input("Enter a number :"))    
# table=[n*i for i in range(1,11)]
# print(table)
# #problem no 4
# try:
#   a=int(input("Enter a number :"))
#   b=int(input("Enter a number :"))
#   print(a/b)
# except ZeroDivisionError as e:
#   print("infinite")  

#problem no 5
n=int(input("Enter a number :"))    
table=[n*i for i in range(1,11)]
with open ("table.txt","a") as f:
  f.write(f"table of {n} is {str(table)} \n")





