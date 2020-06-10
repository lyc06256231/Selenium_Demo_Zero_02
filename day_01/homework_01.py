# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
import random, string, os

gc = webdriver.Chrome() # 初始化浏览器

gc.get("http://192.168.5.99/bbs")
gc.maximize_window() # 最大化窗口
sleep(1)

rand_word = "".join(random.choice(string.ascii_letters + string.digits) for i in range(4)) # hVF1
print(f"rand_word : {rand_word}") # rand_word : hVF1

for i in range(3):
    WebDriverWait(gc, 10, 0.5).until(lambda gc: gc.find_element(By.XPATH, "(//a[text()='立即注册'])[2]"))

    # 点击 立即注册
    gc.find_element(By.XPATH, "(//a[text()='立即注册'])[2]").click()
    sleep(1)
    # 输入注册信息并提交
    print(f"user_{rand_word}_{i}") # user_hVF1_0 user_hVF1_1 user_hVF1_2
    gc.find_element(By.XPATH, "//label[contains(text(),'用户名:')]/../../td/input")\
        .send_keys(f"user_{rand_word}_{i}")
    gc.find_element(By.XPATH, "//label[contains(text(),'密码:')]/../../td/input")\
        .send_keys("123456")
    gc.find_element(By.XPATH, "//label[contains(text(),'确认密码:')]/../../td/input")\
        .send_keys("123456")
    gc.find_element(By.XPATH, "//label[contains(text(),'Email:')]/../../td/input")\
        .send_keys(f"user_{rand_word}_{i}@bbs.com")
    sleep(0.5)
    gc.find_element(By.XPATH, "//strong[contains(text(),'提交')]").click()
    # 点击退出
    WebDriverWait(gc, 10, 0.5).until(lambda gc: gc.find_element(By.XPATH, "//a[text()='退出']"))
    gc.find_element(By.XPATH, "//a[text()='退出']").click()

WebDriverWait(gc, 10, 0.1).until(lambda gc: gc.find_element(By.ID, "ls_username"))
gc.find_element(By.ID, "ls_username").send_keys("admin")
gc.find_element(By.ID, "ls_password").send_keys("123456")
sleep(0.5)
gc.find_element(By.XPATH, "//em[text()='登录']").click()
sleep(1)
gc.find_element(By.XPATH, "//a[text()='管理中心']").click()
sleep(1)
gc.switch_to.window(gc.window_handles[1])
try:
    gc.find_element(By.NAME, "admin_password").send_keys("123456")
    gc.find_element(By.NAME, "admin_password").send_keys(Keys.ENTER)
    sleep(1)
except:
    print("无密码进入管理中心")

# if gc.title == "登录管理中心":
#     gc.find_element(By.NAME, "admin_password").send_keys("123456")
#     gc.find_element(By.NAME, "admin_password").send_keys(Keys.ENTER)
#     sleep(1)

gc.find_element(By.ID, "header_user").click()
sleep(0.5)
gc.switch_to.frame("main")
sleep(0.5)
gc.find_element(By.NAME, "username").send_keys(f"*{rand_word}*")
gc.find_element(By.XPATH, "//input[@value='搜索' and contains(@title,'修改')]").click()
sleep(1)
gc.execute_script("window.scrollTo(0, 210)")
sleep(0.5)
gc.switch_to.default_content()

if not os.path.exists("screenshots"):
    os.mkdir("screenshots")
file_path = f"screenshots/{strftime('%Y-%m-%d %H-%M-%S')}.png"
print(f"scr_path : {file_path}")
gc.save_screenshot(file_path)

gc.switch_to.window(gc.window_handles[0])
sleep(0.5)
gc.find_element(By.XPATH, "//a[text()='默认版块']").click()
sleep(0.5)
gc.find_element(By.XPATH, "(//img[@alt='发新帖'])[1]").click()
sleep(0.5)
gc.find_element(By.ID, "subject").send_keys(f"zero_ui_auto_{strftime('%Y-%m-%d %H-%M-%S')}")
gc.find_element(By.ID, "e_image").click()
sleep(0.5)
gc.find_element(By.ID, "imgattachnew_1").send_keys(f"D:/PythonProjects/Selenium_Demo_Zero_02/day_01/{file_path}")
sleep(0.5)
gc.find_element(By.XPATH, "(//span[text()='上传'])[1]").click()
sleep(2)
gc.execute_script("hideAttachMenu('image')")
sleep(0.5)
gc.switch_to.frame("e_iframe")
with open(__file__, encoding="utf-8") as f:
    post = f.read()
    gc.find_element(By.CSS_SELECTOR, "body").send_keys(post)
    sleep(1)
gc.switch_to.default_content()
gc.find_element(By.ID, "postsubmit").click()