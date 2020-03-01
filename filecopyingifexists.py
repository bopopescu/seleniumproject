import os
fname=input("Enter the file name:")
if os.path.isfile("C://Users/amruth/Desktop/Hemraj/"+fname):
    print("File already exists",fname)
    f1=open("C://Users/amruth/Desktop/Hemraj/"+fname,'r')
    f2=open("C://Users/amruth/Desktop/Hemraj/hemraj.txt",'w')
    f2.write(f1.read())
    f1.close()
    f2.close()
else:
    print("file doesn't exist")

