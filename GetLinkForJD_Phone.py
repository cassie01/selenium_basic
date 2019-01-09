#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 13:46
# @Author  : Cassie
# @File    : GetLinkForJD_Phone.py
# @Software: PyCharm Community Edition
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&ev=exbrand_%E9%AD%85%E6%97%8F%EF%BC%88MEIZU%EF%BC%89%5E&uc=0#J_searchWrap")
# link = driver.find_elements_by_css_selector("#J_goodsList > ul > li")
link = driver.find_elements_by_css_selector("#J_goodsList > ul > li")#获取链接个数
num = len(link)
print(num)
# all_window = driver.window_handles
# print(len(all_window))
# link[0].click()
#J_goodsList > ul > li:nth-child(6) > div > div.p-name.p-name-type-2


for index in range(num):
    i = index + 1
    css = "#J_goodsList > ul > li:nth-child("+str(i)+") > div > div.p-name.p-name-type-2>a"
    img = driver.find_element_by_css_selector(css)
    img.click()
    time.sleep(2)
    all_windows = driver.window_handles#所有的界面
    # print(len(all_windows))
    driver.switch_to.window(all_windows[1])#切换到第二个界面
    driver.close()#关闭tab界面
    driver.switch_to.window(all_windows[0])#切换回第一个界面

driver.quit()