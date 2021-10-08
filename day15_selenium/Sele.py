from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http:ww.baidu.com')
driver.maximize_window()
#寻找搜索输入框
driver.find_element_by_id("kw").send_keys("java")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='kw']").send_keys('aaa')
time.sleep(2)
# 点击百度一下按钮
driver.find_element_by_id("su").click()

time.sleep(3)
# 退出浏览器


driver.quit()

