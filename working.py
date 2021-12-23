import openpyxl
# OPENING AND LOADING A WORKBOOK
wb = openpyxl.load_workbook('MarksList.xlsx')  # loading workbook
worksheet = wb.active  # storing current active worksheet into a variable
print(worksheet)  # printing current worksheet

# acessing cell values
print(worksheet['A1'].value)
print(worksheet['A2'].value)
print(worksheet['B2'].value)

# changing values
worksheet['A2'].value = "New Name"

# save this workbook

wb.save("MarksList.xlsx")