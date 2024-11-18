#list
friends=["laiba","orange",5,35.8,"yousuf"]
print(friends[1])
friends[1]="grapes"
print(friends[1])
#list method
friend=["laiba","orange",5,35.8,"yousuf"]
friend.append("apple")
print(friend)

l1=[1,6,87,3,45]
l1.sort()
print(l1)

l1=[1,6,87,3,45]
l1.reverse()
print(l1)

l1=[1,6,87,3,45]
l1.insert(2,333)
print(l1)

l1=[1,6,87,3,45]
print(l1.pop(2))
print(l1)

l1=[1,6,87,3,45]
l1.remove(45)
print(l1)

#tuple
b=(1,"laiba","orange",5,35.8,5,"yousuf")
print(b)
print(type(b))

no=b.count(5)
print(no)

i=b.index(5)
print(i)

print(len(b))

sliced=b[1:4]
print(sliced)

