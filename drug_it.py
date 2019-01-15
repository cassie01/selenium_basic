#coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 17:30
# @Author  : Cassie
# @File    : drug_it.py
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


# driver.get('https://login.zhipin.com/?ka=header-login')

# icon = driver.find_element_by_id('nc_2_n1z')#########不能用id定位，会发生变化
# icon = driver.find_element_by_css_selector('form>div:nth-child(4) div.nc_scale > span.nc_iconfont.btn_slide')
#滑块移动  click_and_hold
# ActionChains(driver).move_to_element(icon).click_and_hold().move_by_offset(495, 0).release().perform()
# action = ActionChains(driver)
# action.move_to_element(icon)
# action.click_and_hold()
# action.move_by_offset(495, 0)
# action.release()
# action.perform()
driver.get('https://baidu.com')
elem = driver.find_element_by_id('kw')
#右击
# ActionChains(driver).context_click(elem).perform()
#双击没有反应，没有找到合适的场景
# ActionChains(driver).move_to_element(elem).send_keys('金丝熊').click(elem).double_click(elem).perform()
