# -*- coding:utf-8 -*-
from xlwt import Workbook
import json

file = open('student.txt','rb')
text = file.read().decode('gbk')
js = json.loads(text)#将json字符串转换为字典类型
'''
json.load()从文件中读取json字符串

json.loads()将json字符串转换为字典类型

json.dumps()将python中的字典类型转换为字符串类型

json.dump()将json格式字符串写到文件中
'''
book = Workbook()
sheet = book.add_sheet('student')
rownum = 0
js2 = sorted(js)#对所有可迭代的对象进行排序操作
for i in js2:
    colnum = 0
   # print i
    sheet.write(rownum,colnum,i)
    for item in js[i]:
        #print item
        colnum += 1
        sheet.write(rownum,colnum,item)
    rownum += 1
book.save('student.xls')
