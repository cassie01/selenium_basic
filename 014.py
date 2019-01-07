#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 10:28
# @Author  : Cassie
# @File    : 014.py
# @Software: PyCharm Community Edition

import requests,base64
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://persons.shgjj.com/")
time.sleep(2)
driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()
img_eles = driver.find_element_by_xpath('//*[@id="img1"]')
img_eles.screenshot('./img.png')

#client_id 为AK  client_secret为SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=uPatKLisradfOT5EDeuNS83j&client_secret=LhjG9hZ40EcqXC4U3aNVA6697nxXy1AN'
res = requests.get(host)
r = res.json()
print(r)
#获取百度API的token
access_token = r['access_token']#???
print(access_token)

#access_token为调用接口获取的token
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+ access_token
#以二进制方式打开图片文件
f = open(r'./img.png', 'rb')

#参数image:图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
imager = requests.post(url, data = params)
image_json = imager.json()
print(imager.json())


image_num = image_json['words_result'][0]['words']# 对比imager.json，拿到word对应的value
driver.find_element_by_id('imagecode1').send_keys(image_num)


