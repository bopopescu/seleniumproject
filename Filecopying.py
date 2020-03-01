import os
file=input("Enter the file to search:")
if os.path.isfile("C://Users/amruth/Desktop/Hemraj/"+file):
    print("file exists",file)
    f1=open("C://Users/amruth/Desktop/Hemraj/"+file,'r')
    print(f1.read())
else:
    print(file,"named file doesn't exist")