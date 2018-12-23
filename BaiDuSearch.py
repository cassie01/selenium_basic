from  selenium import webdriver
import time 
driver = webdriver.Chrome()
def BrowerSearch(url, selector, keywords, picname):
    driver.get(url)
    if selector == 'kw' :
        driver.find_element_by_id(selector).send_keys(keywords)
    elif selector == 'q':
        driver.find_element_by_name(selector).send_keys(keywords)    
    else:
        print('暂不支持。。')
    driver.save_screenshot(picname)
BrowerSearch('https://baidu.com','kw','王力宏','./baidu.png')
time.sleep(3)
BrowerSearch('https://cn.bing.com','q','Christmas','./santa.png')
time.sleep(3)
driver.quit()
