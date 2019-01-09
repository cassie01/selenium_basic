#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 16:03
# @Author  : Cassie
# @File    : GetLinkForJD_Phone.py
# @Software: PyCharm Community Edition
#依次按链接
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
link = driver.find_elements_by_class_name('mnav')
num = len(link)
print(num)
# for i in range(num):#
#     link = driver.find_elements_by_class_name('mnav')
#     link[i].click()
#     driver.back()
#     time.sleep(2)
#
for index in range(num):
    i = index + 1
    css = "#u1>a:nth-child('+str(i)+')"
    driver.find_element_by_css_selector(css).click()
    driver.back()
    # time.sleep(2)

# for index in range(num):
#     i = index + 1
#     css = "#u1>a:nth-child("+str(i)+")"
#     driver.find_element_by_css_selector(css).click()
#     driver.back()

