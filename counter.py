from collections import Counter
a=[1,2,4,5,1,3,2,7,8,4,1,2,3,2,1,3]
b=Counter(a)
print(b)
print(list(b.elements()))
print(b.most_common())
sub={3:1,8:1}
print(b.subtract(sub))
print(b.most_common())
