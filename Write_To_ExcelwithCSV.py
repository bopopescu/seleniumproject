import csv
with open("C://Users/amruth/Desktop/Hemraj/Student_info.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['NAME','ROLL-NUMBER','MARKS','AGE'])
    while True:
        name=input("Enter the name:")
        roll_no=int(input("Enter the roll number:"))
        marks=int(input("Enter the marks:"))
        age=int(input("Enter the age:"))
        w.writerow([name,roll_no,marks,age])
        option=input("Let me know if you want to enter one more record[Y|N]:")
        if option.lower()=='n':
            break
print("Data successfully entered")