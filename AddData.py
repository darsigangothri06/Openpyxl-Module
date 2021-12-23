import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

wb = openpyxl.Workbook()
# DATA
data = {
    "ONE":{
        "sub1" : 90,
        "sub2" : 89,
        "sub3" : 67,
        "sub4" : 78
    },
    "TWO":{
        "sub1" : 78,
        "sub2": 89,
        "sub3" : 67,
        "sub4" : 65
    }
}

ws = wb.active
ws.title = "GRADES"
headings = ['NUMBER'] + list(data['ONE'].keys())
ws.append(headings)
for person in data:
    grades = [person] + list(data[person].values())
    ws.append(grades)
wb.save("AddfromPy.xlsx")