from openpyxl import load_workbook

RANGE_NAME = 'images'

filepath = "book.xlsx"

wb=load_workbook(filepath)

sheet= wb.active

data = [['Image Folder', 'Image ID']]
data.append(['123','sadada'])

for row in data:
    sheet.append(row)

wb.save(filepath)