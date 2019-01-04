#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:08
# @Author  : Cassie
# @File    : 011.py
# @Software: PyCharm Community Edition
import  xlrd
book = xlrd.open_workbook("LVP Issue List for basic mode.xls")
print("the number of worksheet is {0}".format(book.nsheets))#打印sheet数量
print("worksheet name is : {0}".format(book.sheet_names()))#打印sheet name
sh = book.sheet_by_index(0)#指定在第一个sheet里面
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))#sheet name  ,行数，列数
print("Cell D4 ID {0}".format(sh.cell_value(rowx = 3, colx =3)))
for rx in range(sh.nrows):#打印所有行
    print(sh.row(rx))

