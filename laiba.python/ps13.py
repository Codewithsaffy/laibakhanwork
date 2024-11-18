# # #problem no 1
# # name=(input("Enter your name :"))
# # marks=(input("Enter your marks :"))
# # phone=(input("Enter your phone number :"))

# # s="the name of the student is {} ,and marks is {}, and phone number is {}".format(name,marks,phone)
# # print(s)
# # #problem no 2
# # n=int(input("Enter a number :"))
# # table=[str(n*i) for i in range(1,11)]
# # s="\n" .join(table)
# # print(s)
# #problem no 3
# def divisible5(n):
#   if(n%5==0):
#     return True
#   return False
# a=list(filter(divisible5,range(1,101))) 
# print(a) 

# #problem no 4
# from functools import reduce
# l=[1,2,3,45,5,1872702,77,84,3948,249,492198]
# def greater(a,b):
#   if(a>b):
#     return a
#   return b
# print(reduce(greater,l))  
# #problem no 5
# from flask import Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)


