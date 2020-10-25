# -*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/3/22

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import subprocess
import threading
import traceback


# chrome.exe --start-maximized --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

# os.system('chrome.exe --start-maximized --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
# subprocess.call('chrome.exe --start-maximized --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')

# class myThread (threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         print ("开始线程：")
#         run_bat()
#         print ("退出线程：")
def run_bat():
    bat_path = os.path.dirname(os.path.abspath(__file__))

    subprocess.call(os.path.join(bat_path, 'run_chrom.bat'))


# thread1 = myThread()
# thread1.start()

# run_bat()
# option = webdriver.ChromeOptions()
# print(11)
# time.sleep(5)
option = Options()
# option.add_argument('--enable-hung-renderer-infobar') # 'disable-infobars'失效，采用命令行创建窗口的方式，不会出现"正在受到自动软件的控制"的信息栏提示
# option.add_argument('--silent-debugger-extension-api') # 'disable-infobars'失效，采用命令行创建窗口的方式，不会出现"正在受到自动软件的控制"的信息栏提示
# option.add_argument('--silent-debugger-extension-api') # 'disable-infobars'失效，采用命令行创建窗口的方式，不会出现"正在受到自动软件的控制"的信息栏提示

# option.add_experimental_option("excludeSwitches", ['enable-automation']) # 出现＂请停用以开发者模式运行的扩展程序＂

option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# print(option.experimental_opstions)

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


driver = webdriver.Chrome(
    # executable_path=r"C:\programs\python\Python37-32\chromedriver.exe",\
    options=option)

driver.implicitly_wait(5)

driver.get("http://www.baidu.com")

print(driver.title)

ac = ActionChains(driver)

# 鼠标移动到 元素上
ac.move_to_element(
    driver.find_element_by_css_selector('[name="tj_briicon"]')
).perform()

ac.click(
    driver.find_element_by_css_selector('[name="tj_img"]')
).perform()

driver.get('http://cdn1.python3.vip/files/selenium/test4.html')


# --- alert ---
driver.find_element_by_id('b1').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)
alert = driver.switch_to.alert

# 点击 OK 按钮
driver.switch_to.alert.accept()

driver.set_page_load_timeout()

# driver.find_element_by_id("kw").send_keys("令才qq")
# driver.find_element_by_id("su").click()


# animals = driver.find_element_by_id('inner11').parent
# print(animals)
# print(animals.get_attribute('outerHTML'))
# print('===')
# print(animals.get_attribute('innerHTML'))

# print(driver.get_att)


driver.quit()
