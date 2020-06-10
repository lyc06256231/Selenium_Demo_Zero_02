# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, strftime

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get(r"file:///E:/RF_Project/RF_Demo_02/Test_Selenium.html")
driver.maximize_window()
sleep(1)

str_time = strftime("%Y-%m-%d %H-%M-%S")
driver.save_screenshot(f"E:/UI_Auto_ScreenShots/{str_time}.png")