import csv
f=open("C://Users/amruth/Desktop/Hemraj/foperation.csv",'r')
r=csv.reader(f)
data=list(r)
for r in data:
    for c in r:
        print(c,end='     ')
    print()