# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get(r"file:///E:/RF_Project/RF_Demo_02/Test_Selenium.html")
driver.maximize_window()
sleep(1)

driver.switch_to.frame("s_iframe")

bj_url = driver.find_element(By.LINK_TEXT, "学习笔记").get_property("href")
print(bj_url)

# driver.switch_to.default_content() # 切换到最顶部的frame
driver.switch_to.parent_frame() # 切换到上一级的frame

driver.find_element(By.XPATH, "//input[@value='点我测试alert弹框']").click()