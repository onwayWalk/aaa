from selenium import webdriver
import time

webdriver=webdriver.Chrome()
webdriver.get(r"http:\\www.jd.com")
webdriver.maximize_window()

webdriver.find_element_by_xpath("//*[@class='lazyimg_img']").click()
window=webdriver.window_handles
webdriver.switch_to.window(window[-1])
time.sleep(3)
webdriver.find_element_by_xpath("//*[@id='super_seckill']/div/ul/li[1]").click()
# webdriver.find_element_by_xpath("/html/body/div[3]/div[5]/div[5]/div[2]/div/ul/li[1]/a/img").click()
time.sleep(5)
webdriver.quit()