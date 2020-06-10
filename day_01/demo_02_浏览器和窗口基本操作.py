# coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://baidu.com")
sleep(1)

driver.maximize_window() # 最大化浏览器窗口
sleep(1)

print(driver.title) # 获取窗口标题

# driver.refresh() # 刷新页面
# sleep(1)
#
# driver.get("https://jd.com") # 在当前窗口打开一个链接
# sleep(1)

# driver.back() # 返回上一级
# sleep(1)
#
# driver.forward() # 前进

# driver.minimize_window() # 最小化窗口 了解即可
# driver.fullscreen_window() # 网页全屏 了解即可