#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 10:18
# @Author  : Cassie
# @File    : 013.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import xlwt

driver = webdriver.Chrome()
driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=890235b1e5fc48bdb3e18ef30443baca")
price = driver.find_elements_by_css_selector("li.gl-item div.gl-i-wrap div.p-price")
phone_name  = driver.find_elements_by_css_selector("div.p-name.p-name-type-2")
# print(len(elems))
count = len(price)
wd = xlwt.Workbook()
ws = wd.add_sheet("jd_手机")

ws.write(0, 0, '手机')
ws.write(0,1, "价格")

for index in range(count):
    ws.write(index+1, 0,phone_name[index].text)
    ws.write(index+1, 1, price[index].text)

wd.save("phone.xls")