from zipfile import *
f=ZipFile("C://Users/amruth/Desktop/Hemraj/hemraj.zip",'w',ZIP_DEFLATED)
f.write("C://Users/amruth/Desktop/Hemraj/bucket2.txt")
f.write("C://Users/amruth/Desktop/Hemraj/bucket3.txt")
f.close()