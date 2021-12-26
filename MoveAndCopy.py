import openpyxl

filename = "MovePractice.xlsx"
wb = openpyxl.Workbook()
ws = wb.active

def print_rows(ws):
    rowS = ''
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            rowS += "{:<3}".format(str(cell.value) + '  ')
        rowS += '\n'
    print(rowS)
    print('*'*20)
    
# def SetValues(ws):
ws.delete_cols(1,100)