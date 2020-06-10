# coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://baidu.com")
sleep(1)

driver.maximize_window() # 最大化浏览器窗口
sleep(1)
print(driver.title)

driver.find_element(By.LINK_TEXT, '设为首页').click()
sleep(1)
print(driver.title)

'''
窗口切换
1：driver.window_handles 获取所有窗口句柄
2：driver.switch_to.window(handles_list[1]) 根据索引切换到对应窗口
'''
handles_list = driver.window_handles

driver.switch_to.window(handles_list[1])
print(driver.title)