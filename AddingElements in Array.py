from array import *
a=array('i',[1,2,3])
print(a)
a.append(4)
print(a)

b=array('i',[4,5,6])
print(b)
b.extend([7,8,9])
print(b)

c=array('i',[10,12,13])
print(c)
c.insert(1,11)
print(c)

c.remove(13)
print(c)