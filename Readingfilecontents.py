import os
fname=input("enter the file name:")
if os.path.isfile("C://Users/amruth/Desktop/Hemraj/"+fname):
    print("File exists",fname)
    lcount=wcount=ccount=0
    f=open("C://Users/amruth/Desktop/Hemraj/"+fname,'r')
    for line in f:
        lcount=lcount+1
        word=line.split()
        wcount=wcount+len(word)
        ccount=ccount+len(line)
    print("number of lines:",lcount)
    print("number of words:", wcount)
    print("number of characters:", ccount)
else:
    print("File doesn't exist",fname)
