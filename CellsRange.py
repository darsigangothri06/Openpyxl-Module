import openpyxl

wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active
cellr = ws['A8':'C11']
print(cellr)
for row in cellr:
    for col in row:
        print(col,col.value)