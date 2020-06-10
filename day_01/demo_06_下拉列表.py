# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # 下拉列表
from time import sleep

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get(r"file:///E:/RF_Project/RF_Demo_02/Test_Selenium.html")
driver.maximize_window()
sleep(1)

select_ele = Select(driver.find_element(By.NAME, "fruit"))

select_ele.select_by_index(3) # 根据索引
sleep(1)
select_ele.select_by_value("volvo") # 根据value值
sleep(1)
select_ele.select_by_visible_text("苹果") # 根据文本内容