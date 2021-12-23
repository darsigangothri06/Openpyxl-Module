import openpyxl

wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active

ws.insert_rows(4)  # insert an empty row at row 4

wb.save("MarksList.xlsx")