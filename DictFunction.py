d={'Hem':'001','Raj':'002','Karu':'003'}
print(d)
d['Hem']='004'  #replace value to a key
print(d)
d['vinamane']='005' #adding new key value
print(d)
print(d.get('Raj'))
print(d.keys())
print(d.values())
for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for x,y in d.items():
    print(x,y)

#deleting
d.pop('Hem')
print(d)
d.popitem()
print(d)
del d['Karu']
print(d)