import openpyxl

wb = openpyxl.load_workbook("MarksList.xlsx")
ws = wb.active
print(ws)
print(wb['Sheet2'])
print(wb.sheetnames) # printing active sheetnames

# creating a new sheet

wb.create_sheet("NEWSHEET")
print(wb.sheetnames)