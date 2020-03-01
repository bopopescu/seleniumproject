string="Hi how are you today at office sunday"
print(string)
print(type(string))

l=string.split()
print(l)
print(type(l))

new_dict={}
for x in range(0,len(l),2):
    new_dict[l[x]]=l[x+1]
print(new_dict)