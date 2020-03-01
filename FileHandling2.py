import os
f=open("C:/Users/amruth/Desktop/Hemraj/bucket2.txt",'w')  # this will override all data in text file
f.write("Hi this is hemraj\n")
f.write("Today is wednesday\n")
f.write("I am in banglore")
f.close()

import os
f=open("C:/Users/amruth/Desktop/Hemraj/bucket3.txt",'w')
f.writelines("Bucket3 is a New file\n")
f.write("Next line added")
f.close()
