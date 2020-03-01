import os
f=open("C:/Users/amruth/Desktop/Hemraj/bucket2.txt",'r') # this will just read all the data
print(f.read())
f.close()


import os
f=open("C:/Users/amruth/Desktop/Hemraj/bucket2.txt",'r')   # this will just read first line
print(f.readline())
f.close()

import os
f=open("C:/Users/amruth/Desktop/Hemraj/bucket2.txt",'r')  # this will  read all the data in list format
print(f.readlines())
f.close()


