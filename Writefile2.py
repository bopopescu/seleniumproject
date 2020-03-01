import openpyxl

path="C:/Users/amruth/Desktop/Hemraj/Write.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active
for r in range(1,4):
    for c in range(1,3):
        sheet.cell(row=r,column=c).value="hemraj"

workbook.save(path)