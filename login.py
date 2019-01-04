#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 16:30
# @Author  : Cassie
# @File    : login.py
# @Software: PyCharm Community Edition

import unittest
from selenium import webdriver
"""

"""

class Cnode(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)

    def test_register(self):
        driver = self.driver
        driver.find_element_by_css

    def test_login(self):
        pass

    def tearDown(self):
        self.driver.save_screenshot('./01.png')
        self.driver.quit()