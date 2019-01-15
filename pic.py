#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:17
# @Author  : Cassie
# @File    : pic.py
# @Software: PyCharm Community Edition

#文件的上传及截图操作

from selenium import webdriver
# from os import path

driver = webdriver.Chrome()
#
# #定义截图存储的路径
# d = path.dirname(__file__)
# index = path.join(d,'index.png')
# image = path.join(d,'image.png')
#
# driver = webdriver.Chrome()
#
driver.get("https://www.baidu.com/")
#
# #百度首页截图保存的路径名
# driver.save_screenshot('./index.png')
#
driver.find_element_by_class_name('soutu-btn').click()
#
# # 上传图片截图保存的路径名
# driver.save_screenshot('./image.png')

# 点击本地上传按钮，后面的路径是windows中的路径格式（注释：此处是我的电脑中图片的路径名）
driver.find_element_by_class_name('upload-pic').send_keys('C:\\Users\\Public\\Pictures\\Sample Pictures\\01.jpg')



# from selenium import webdriver
#
#

#
#
# driver.get('http://39.107.96.138:3000/signin')
# driver.find_element_by_id('name').send_keys('user1')
# driver.find_element_by_id('pass').send_keys('123456')
# driver.find_element_by_css_selector('.span-primary').click()
#
# driver.get('http://39.107.96.138:3000/topic/create')
#
# driver.find_element_by_class_name('eicon-image').click()
#
#
# driver.find_element_by_class_name('webuploader-element-invisible').send_keys('/Users/zyzhao/Desktop/2019-01-13-selenium02.png')

