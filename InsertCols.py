import openpyxl

wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active

# ws.insert_cols(2)
ws.delete_cols(2)

wb.save("MarksList.xlsx")