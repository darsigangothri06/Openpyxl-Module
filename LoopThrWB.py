# looping through an excel file

import openpyxl
from openpyxl.utils import get_column_letter
wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active  # active sheetname

for row in range(1,6):
    for col in range(1,2):
        char = get_column_letter(col)
        print(ws[char + str(row)].value)