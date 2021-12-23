import openpyxl

wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active

ws.move_range("D3:E7", rows = 2, cols = 2)

wb.save("MarksList.xlsx")