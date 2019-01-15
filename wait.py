#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:41
# @Author  : Cassie
# @File    : wait.py
# @Software: PyCharm Community Edition


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# driver.implicitly_wait(10)

driver.get('https://outlook.live.com/owa/#')
driver.find_element_by_css_selector('div.headerContainer>div>a').click()
# inputemail = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('loginfmt'))
inputemail = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
inputemail.send_keys('dasdasdas')



