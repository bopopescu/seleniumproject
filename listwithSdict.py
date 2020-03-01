nl=['name','hemraj','salary','40k','age','30','city','shimoga']
new_dict={}
for i in range(0,len(nl),2):
    new_dict[nl[i]]=nl[i+1]
print(new_dict)

