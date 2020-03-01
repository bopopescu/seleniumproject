import os
for dircspath,dircsfolder,filename in os.walk('C://Users/amruth/Desktop/Hemraj'):
    print("Directory name:",dircspath)
    print("Folder name:",dircsfolder)
    print("Number of files:",filename)
    print()
    print()