from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path="./chromedriver.exe")#传入路径有两种方式
driver = webdriver.Chrome()#打开浏览器，把chrome放入与python同级目录，括号内不需要添加执行路径。
def openBaiDu(url, selector, keyword,pic):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id(selector).send_keys(keyword)
    else:
        driver.find_element_by_name(selector).send_keys(keyword)
    driver.save_screenshot(pic)#截屏

openBaiDu('https://baidu.com','kw','王力宏','./baidu.png')  #绝对路径
time.sleep(3)
driver.quit()#退出diver.close()是关闭tab页