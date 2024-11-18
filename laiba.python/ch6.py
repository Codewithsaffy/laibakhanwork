#if else statement
# a=int(input("Enter a number :"))

# if(a>=18):
#   pr0):int("You are eligible to vote")
#   print("Please cast your vote")

# else:
#   print("You are not eligible to vote")
  #if elif else statement
a=int(input("Enter a number :"))

if(a>=18 ):
  print("You are eligible to vote")
  print("Please cast your vote")
elif(a<0):
  print("Please enter a valid age")  
elif(a==0):
  print("You are entered 0 which is not valid age")  
else:
  print("You are not eligible to vote")