import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
cnt = 1
for row in range(1,11):
    for col in range(1,11):
        ws.cell(row = row, column = col).value = cnt
        cnt += 1

# Inserting rows
ws.insert_rows(0)
ws.merge_cells("A1:J1")
ws.cell(row = 1, column=1).value = "NUMBERS"

wb.save("Numbers.xlsx")