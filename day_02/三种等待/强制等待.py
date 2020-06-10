# coding=utf-8

'''
sleep : 睡眠
使线程暂停指定秒数（强制）
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

gc = webdriver.Chrome()

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()
sleep(1)

gc.find_element(By.XPATH, "//input[@value='测试等待']").click()
sleep(3.1)
gc.find_element(By.ID, "test_input_01").send_keys("66666")