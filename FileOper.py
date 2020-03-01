import csv
f=open("C://Users/amruth/Desktop/Hemraj/foperation.csv",'w',newline='')
w=csv.writer(f)
w.writerow(['Name','EmpID','Salary','Age'])
while True:
    name=input("Enter the name:")
    empid=int(input("Enter the ID:"))
    salary=int(input("Enter the salary:"))
    age=int(input("Enter the age"))
    w.writerow([name,empid,salary,age])
    choice=input("Do you want to insert one more record[Y|N]:")
    if choice.lower()=='n':
        break
print("Information entered successfully ")