# l=open("file.txt","r")
# data=l.read()
# print(data)
# l.close()

# st="you are a good "
# f=open("file1.txt","w")
# f.write(st)
# f.close()

# l=open("file.txt","r")
# line1=l.readline()
# print(line1,type(line1))
# line2=l.readline()
# print(line2,type(line2))
# line3=l.readline()
# print(line3,type(line3))
# l.close()
#or aise bhi likh sakte hai
# line=l.readline()
# while (line != ""):
#   print(line)
#   line=l.readline()
# l.close()  
#append mood file ke end me add karne ke leye istamal hota hai
# st="I am a good"
# f=open("file.txt","a")
# f.write(st)
# f.close()
#with laga ke hum ye ker sakte hai
# with open("file.txt","r") as f:
#   print(f.read())
#or dosra tareka ye bhi hai
f=open("file.txt","r")
print(f.read())
f.close()
