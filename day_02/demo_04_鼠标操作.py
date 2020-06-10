# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

gc = webdriver.Chrome()

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()
sleep(1)

ActionChains(gc)\
    .double_click(gc.find_element(By.XPATH, "//input[@value='测试双击']"))\
    .context_click(gc.find_element(By.XPATH, "//input[@value='测试右击']"))\
    .perform()

