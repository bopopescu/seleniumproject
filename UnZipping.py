from zipfile import *
f=ZipFile("C://Users/amruth/Desktop/Hemraj/File7.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("File name is :",name)
    f1=open("C://Users/amruth/Desktop/Hemraj/"+name,'r')
    print("The contents of file are:")
    print(f1.read())
    print('*'*10)
