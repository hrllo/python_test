import xlwt,json

with open('source/0015/city.txt','r') as f:
    data = json.load(f)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
    for index, (key, value) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        sheet1.write(index, 1, value)
    workbook.save('source/0015/city.xls')