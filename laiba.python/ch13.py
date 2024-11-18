#lambda
stuare=lambda x: x*x
print(stuare(5))
add=lambda x: x+x
print(add(5))
sub=lambda x: x-x
print(sub(5))
#join string
a=["laiba","areeba","yousuf","younus"]
final="_".join(a)
print(final)
#format 
a="{0} is a good {1}".format ("laiba","girl")
print(a)
#map
a=[1,2,3,4,5]
square=list(map(lambda x: x*x,a))
print(square)
#filter
def even (n):
  if n%2==0:
    return True
  return False
a=[1,2,3,4,5,6,7,8,9,10]
even_num=list(filter(even,a))
print(even_num)
#reduce
from functools import reduce
def add (a,b):
  return a+b
mul =lambda x,y: x*y  
print(reduce(add,a))  
print(reduce(mul,a))  
