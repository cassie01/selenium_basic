#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:45
# @Author  : Cassie
# @File    : OpenKnow.py
# @Software: PyCharm Community Edition

import selenium
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class OpenKnow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.zhihu.com/signup?next=%2F")

    def test_login(self):
        driver = self.driver
        phone = driver.find_element_by_name("phoneNo")
        ActionChains(driver).move_to_element(phone).click().send_keys("13709783628").perform()#
        time.sleep(3)
        driver.find_element_by_css_selector("button[class = 'Button CountingDownButton SignFlow-smsInputButton Button--plain']").click()

        # driver.find_element_by_class_name("Button CountingDownButton SignFlow-smsInputButton Button--plain").click()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()