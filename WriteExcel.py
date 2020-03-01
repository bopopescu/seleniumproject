import openpyxl
path="C:/Users/amruth/Desktop/Hemraj/New.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active
sheet.title="Data_info"
rows=int(input("Enter the number of rows:"))
colms=int(input("Enter the number of columns:"))
print(rows)
print(colms)

for r in range(1,rows+1):
    for c in range(1,colms+1):
        data=input("Enter data:")
        sheet.cell(row=r,column=c).value=data
workbook.save(path)