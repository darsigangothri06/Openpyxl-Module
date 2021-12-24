import openpyxl

wb = openpyxl.load_workbook("Inserting.xlsx")
ws = wb.active

newcopy = wb.copy_worksheet(ws)

print(newcopy)
