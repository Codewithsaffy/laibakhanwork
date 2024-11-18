# #problem no 1
# a1 =int(input("Enter number 1 : "))
# a2 =int(input("Enter number 2 : "))
# a3 =int(input("Enter number 3 : "))
# a4 =int(input("Enter number 4 : "))
# if(a1>a2 and a1>a3 and a1>a4):
#   print("a1 is the greatest number",a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#   print("a2 is the greatest number",a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#   print("a3 is the greatest number",a3)
# elif(a4>a1 and a4>a2 and a4>a3):
#   print("a4 is the greatest number",a4)
# #problem no 2
# Marks1=int(input("Enter your Marks  :"))
# Marks2=int(input("Enter your Marks  :"))
# Marks3=int(input("Enter your Marks  :"))
# Total_Percentage = (100*(Marks1+Marks2+Marks3))/300
# if(Total_Percentage>=40):
#   print("You are pass")
# else:
#   print("You are fail")
# #problem no 3
# Marks1=int(input("Enter your Marks  :"))
# Marks2=int(input("Enter your Marks  :"))
# Marks3=int(input("Enter your Marks  :"))
# Total_Percentage = (100*(Marks1+Marks2+Marks3))/300
# if(Total_Percentage>=40 and Marks1>=33 and Marks2>=33 and Marks3>=33):
#   print("You are pass")
# else:
#   print("You are fail")
# #prolem no 4
# p1="buy now"
# p2="subscribe this"
# p3="click this"
# message=input("Enter your comments :")
# if(p1 in message) or (p2 in message) or (p3 in message):
#   print("This is spam")
# else:
#   print("This is not spam")  
# #problem no 5
# username=input("Enter your username :")
# if(len(username)<10):
#   print("Your user name less than 10 characters")
# else:
#   print("All is well!")
# #problem no 6
# l=["Laiba","Areeba","Yousuf","Younus"]
# name=input("Enter your name :")
# if (name in l):
#   print("Your name in the list")
# else:
#   print("Your name not in the list")  
# #problem no 7
# Marks=int(input("Enter your Marks :"))
# if(Marks<=100 and Marks>=90):
#   grade="Ex"
# elif(Marks<90 and Marks>=80):
#   grade="A"
# elif(Marks<80 and Marks>=70):
#   grade="B"
# elif(Marks<70 and Marks>=60):
#   grade="C"
# elif(Marks<60 and Marks>=50):
#   grade="D"
# else:
#   grade="Fail"
 
# print("your grade is",grade)  
#problem no 8
post=input("Enter your post :")
if("Laiba".lower() in post.lower()):
  print("This post is talking about Laiba")
else:  
  print("This post is not talking about Laiba")