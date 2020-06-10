# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get(r"file:///E:/RF_Project/RF_Demo_02/Test_Selenium.html")
driver.maximize_window()
sleep(1)

# 对文件上传元素使用send_keys方法，发送要上传的文件的路径
driver.find_element(By.ID, 'file').send_keys("E:/RF_Project/RF_Demo_02/Test_Selenium.html")