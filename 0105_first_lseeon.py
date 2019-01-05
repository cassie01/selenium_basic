from selenium import webdriver
import unittest
import time

driver = webdriver.Chrome()

# driver.find_element_by_name("tj_trnews").click()
# navs = driver.find_elements_by_class_name("mnav")
# for i in navs:
#     i.click()
#     driver.back()
# for index in range(len(navs)):
#     navs = driver.find_elements_by_class_name("mnav")
#     navs[index].click()
#     driver.back()
#     time.sleep(1)
    
# counter = len(navs)
# for index in range(counter):
#     i = index + 1
#     css = "#u1>a:nth-child("+str(i)+")"
#     driver.find_element_by_css_selector(css).click()
#     driver.back()
# driver.find_element_by_link_text("新闻").click()
# driver.find_element_by_partial_link_text("新").click()
   



def search():
    baidu_input = driver.find_element_by_id("kw")
    baidu_input.send_keys("仓鼠")
    time.sleep(1)
    baidu_input.clear()
    baidu_input.send_keys("金丝熊")
    # driver.find_element_by_class_name("bg s_btn").click()
    driver.find_element_by_id("su").click()

    time.sleep(1)
    content = driver.find_element_by_id("content_left")
    with open("kele.txt",'w', encoding = "utf-8") as f :
        f.write(content.text)

# print(content.text)

# time.sleep(3)
# driver.quit()
###京东
# text = driver.find_element_by_css_selector(".price.J-p-7081550").text
driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=shou%27j&pvid=8efa5cc4abe84804b801a390f641a2eb")
# print("打开首页之后浏览器窗口个数",len(driver.window_handles))
# text1 = driver.find_elements_by_css_selector(".gl-item")#多个元素调用的是elements，而且不需要调用text
# num = len(text1)
# print(num)
img = driver.find_elements_by_css_selector('li.gl-item>div.gl-i-wrap>div.p-img>a:nth-child(1)')
# eles = driver.find_elements_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a")

#####img是一个数组？可遍历的
# num = len(eles)
num = len(img)
print(num)
# img[0].click()
# print("打开第一个之后浏览器窗口个数",len(driver.window_handles))
# all_windows = driver.window_handles
# driver.switch_to_window(all_windows[0])
# img[1].click()
#循环切换手机界面
# for i in range(num) :
#     # img = driver.find_elements_by_css_selector("li.gl-item>div.gl-i-wrap>div.p-img>a:nth-child(1)")
#     driver.maximize_window()#窗口最大化，碍于二维码
#     img[i].click()
#     all_windows = driver.window_handles
#     # print(len(all_windows))
#     # time.sleep(2)
#     driver.switch_to.window(all_windows[1])#切换到第二个
#     time.sleep(2)
#     driver.close() #关闭当前tab
#     driver.switch_to.window(all_windows[0])#切换第一个



    




    
