#发帖
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://39.107.96.138:3000/signin")
driver.find_element_by_xpath("//*[@id='name']").send_keys("user1")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='signin_form']/div[3]/input").click()
driver.find_element_by_xpath("//*[@id='create_topic_btn']/span").click()
driver.find_element_by_xpath("//*[@id='tab-value']/option[2]").click()#存在里面也有引号的问题，要使用单引号
driver.find_element_by_xpath("//*[@id='title']").send_keys("可乐0002")
content = driver.find_element_by_xpath("//*[@class='CodeMirror-scroll']")
ActionChains(driver).move_to_element(content).click().send_keys("test 22222").perform()
driver.find_element_by_xpath("//*[@id='create_topic_form']/fieldset/div/div/div[4]/input").click()