# def func():
#   a=int(input("Enter a number :"))
#   b=int(input("Enter a number :"))
#   c=int(input("Enter a number :"))
#   func=(a+b+c)/3
#   print(func)

# # func()  
# # print("Thank you")
# # func()  
# # print("Thank you")
# # func()  
# # print("Thank you")

# def good_day():
#   print("Good day")
# good_day()  
# # func()

# def goodDay(name , ending):
#   print("Good Day ,"+name)
#   print(ending)
# goodDay("Laiba ","Thank You")
# goodDay("Areeba ","Thank You")
# goodDay("Younus ","Thank You")

# def goodDay(name , ending):
#   print("Good Day ,"+name)
#   print(ending)
#   return "Ok"
# a=goodDay("Laiba ","Thank You")
# print(a)

def goodDay(name , ending="Thank you"):
  print("Good Day ,"+name)
  print(ending)
  return "Ok"
goodDay("Laiba ")
a=goodDay("Laiba ","Thanks")
print(a)


def fact(n):
  if(n==0 or n==1):
    return 1
  return n*fact(n-1)

print(fact(5))