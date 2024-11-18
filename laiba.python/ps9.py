# #problem no 1
# f=open("file.txt","r")
# content=f.read()
# if ("Twinkle" in content):
#   print("The word Twinkle is present in the content")
# else:
#   print("The wordTwinkle is not present in the content")
#   f.close()
  
# #problem no 2
# import random
# def game():
#   print("You are playing a game")
#   score=random .randint(1,61)
#   with open("hiscore.txt") as f:
#     hiscore=f.read()
#     if (hiscore!=""):
#       hiscore=int(hiscore)
#     else:
#       hiscore=0
#   print(f"your score{score}")
#   if(score>hiscore):
#     with open ("hiscore.txt","w") as f:
      
#       f.write(str(score))
#   return score
# game()  
# #problem no 3
# def generate_table(n):
#   table=""
#   for i in range(1,11):
#     table+= f"{n} x {i} = {n*i}\n"

#   with open (f"tables/table_{n}","w") as f:
#     f.write(table)



# for i in range(2, 20):
#   generate_table(i)
# #problem no 4
# word="Donkey"
# with open ("file.txt","r") as f:
#   content=f.read()
#   content_new=content.replace(word,"****")
# with open ("file.txt","w") as f:
#   f.write(content_new)
# #problem no 5
# words="Donkey"
# with open ("file.txt","r") as f:
#   content=f.read()
#   for word in words:
#     content=content.replace(word,"#"*len(word))
# with open ("file.txt","w") as f:
#   f.write(content)

# #problem no 6
# with open ("file.txt") as f:
#   content=f.read()
# if ("python" in content):
#   print("python is preasent")
# else:
#   print("python is not preasent")
# #problem no 7
# with open ("file.txt") as f:
#   lines=f.readlines()
# lineno=1
# for line in lines:
#   if ("python" in line):
#     print(f"python is preasent in line{lineno}")
#     break
#   lineno +=1
# else:
#     print("python is not preasent")
# #problem no 8
# with open ("file.txt") as f:
#   content=f.read()
# with open ("file1.txt","w")as f:
#   f.write(content)  
# #problem no 9
# with open ("file.txt") as f:
#   content1=f.read()
# with open ("file1.txt") as f:
#   content2=f.read()
# if (content1==content2):
#   print("yes this file are identical" )
# else: 
#   print("no this file are notidentical")  
#problem no 10
with open ("file.txt","w") as f:
  f.write("")









