# Changing name of sheet
import openpyxl

wb = openpyxl.load_workbook("Inserting.xlsx")
ws = wb.active
print(ws)  # Master1
ws.title = "MASTERSHEET"
ws1 = wb.active
print(ws1)  # MASTERSHEET

wb.save("Inserting.xlsx")