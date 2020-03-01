l=['a',1,'b',2,'c',3,'a',1,'b',2,'c',3,'a',1,'b',2,'c',3]
print(l)
print(type(l))

s=set()
new_list=[]

for x in l:
    if x not in s:
        s.add(x)
        new_list.append(x)
print(new_list)