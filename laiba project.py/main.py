import random
'''
-1=snake
1=water
0=gun
'''
computer= random.choice([-1, 0, 1])
youstr=input("enter your choice :")
youdict={"snake":-1,"water":1,"gun":0}
reversedict={-1:"snake",1:"water",0:"gun"}
you=youdict[youstr]
print(f"your choice is ({reversedict[you]})\ncomputer choice is ({reversedict[computer]})") 
if (computer==you):
  print("tie")
else:
  if (you==1 and computer==-1) : 
    print("you win") 
  elif (you==0 and computer==-1) : 
    print("you win") 
  elif (you==-1 and computer==1) : 
    print("you lose") 
  elif (you==0 and computer==1) : 
    print("you win") 
  elif (you==-1 and computer==0) : 
    print("you lose") 
  elif (you==1 and computer==0) : 
    print("you lose") 
  else:
    print("some thing went wrong") 
'''
#anoter way
if((computer-you)==-1 or (computer-you)==2):
  print("you lose")     
else:
  ("you win")
  '''







