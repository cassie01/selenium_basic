#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 11:02
# @Author  : Cassie
# @File    : read_weiboContent_excel.py
# @Software: PyCharm Community Edition

#标题  发送人 发送时间+来源  收藏 转发数 评论数 点赞
from selenium import webdriver
import time
import xlwt


#搜索到原创微博
driver = webdriver.Chrome()
# driver.get("https://www.weibo.com/sg")
# driver.find_element_by_name("15470037304342").send_keys("金丝熊")
# driver.find_elements_by_class_name("W_ficon ficon_search S_ficon").click()
# driver.find_elements_by_link_text("高级搜索").click()
# driver.find_element_by_id("radio03").click()
# driver.find_elements_by_link_text("搜索微博").click()
driver.get("https://s.weibo.com/weibo/%25E9%2587%2591%25E4%25B8%259D%25E7%2586%258A?q=%E9%87%91%E4%B8%9D%E7%86%8A&scope=ori&suball=1&Refer=g")

#获取数量20，数量只需要获取一次
title_num = driver.find_elements_by_css_selector("#pl_feedlist_index > div:nth-child(2) > div")
count = len(title_num)
title = driver.find_elements_by_css_selector("div.content p.txt")
sender = driver.find_elements_by_css_selector("div.info a.name")
send_time = driver.find_elements_by_css_selector("div.content>p.from")
collect =driver.find_elements_by_css_selector("div[class='card-act']>ul>li:nth-child(1)")
transmit = driver.find_elements_by_css_selector("div[class='card-act']>ul>li:nth-child(2)")
comments = driver.find_elements_by_css_selector("div[class='card-act']>ul>li:nth-child(3)")
agree = driver.find_elements_by_css_selector("div[class='card-act']>ul>li:nth-child(4)")

#创建每列名称excel
wd = xlwt.Workbook()
ws = wd.add_sheet('微博——金丝熊')
ws.write(0, 0, '标题')
ws.write(0, 1 , '发送人')
ws.write(0, 2, '发送时间+来源')
ws.write(0, 3, '收藏')
ws.write(0, 4, '转发数')
ws.write(0, 5, '评论数')
ws.write(0, 6, '点赞')
#将相关信息写入表格中
for index in range(count):
    i = index + 1
    ws.write(index+1, 0, title[index].text)
    ws.write(index+1, 1, sender[index].text)
    ws.write(index + 1, 2, send_time[index].text)
    ws.write(index + 1, 3, collect[index].text.split('收藏')[1])#split方法
    ws.write(index + 1, 4, transmit[index].text.split('转发')[1])
    ws.write(index + 1, 5, comments[index].text.split('评论')[1])
    ws.write(index + 1, 6, agree[index].text)

wd.save('kele.xls')

