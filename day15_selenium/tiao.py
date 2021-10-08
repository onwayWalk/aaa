from selenium import webdriver
import time
webdriver=webdriver.Chrome()
webdriver.get(r"C:\Users\lenovo\Desktop\搭建7\练习的html\跳转页面\pop.html")
webdriver.maximize_window()
handle=webdriver.current_window_handle

webdriver.find_element_by_xpath("//*[@id='goo']").click()
handle2=webdriver.window_handles

for i in range(10):
    webdriver.switch_to.window(handle2[0])
    time.sleep(1)
    webdriver.switch_to.window(handle2[-1])
    time.sleep(1)
webdriver.quit()