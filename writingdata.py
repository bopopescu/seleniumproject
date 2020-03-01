import openpyxl
path="C:/Users/amruth/Desktop/Hemraj/Write1.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active

for r in range(1,6):
    for c in range(1,6):
        sheet.cell(row=r,column=c).value='python'
workbook.save(path)