# Changing name of sheet
import openpyxl

wb = openpyxl.load_workbook("Inserting.xlsx")
ws = wb.active
print(ws)  # Master1
ws.title = "MASTERSHEET"
ws1 = wb.active
print(ws1)  # MASTERSHEET

# changing the color of sheet
ws1.sheet_properties.tabColor = "85E51D"
ws2 = wb['Master2']
ws2.sheet_properties.tabColor = "e5691d"
wb.save("Inserting.xlsx")