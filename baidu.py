#-*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/3/22

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
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
    subprocess.call(r'C:\code\ChromeSelenium\run_chrom.bat')
# thread1 = myThread()
# thread1.start()

run_bat()
# option = webdriver.ChromeOptions()
print(11)
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



driver = webdriver.Chrome(\
    # executable_path=r"C:\programs\python\Python37-32\chromedriver.exe",\
    options=option)

driver.implicitly_wait(5)

driver.get("http://www.baidu.com")

print(driver.title)

driver.find_element_by_id("kw").send_keys("令才qq")
driver.find_element_by_id("su").click()




# animals = driver.find_element_by_id('inner11').parent
# print(animals)
# print(animals.get_attribute('outerHTML'))
# print('===')
# print(animals.get_attribute('innerHTML'))

# print(driver.get_att)

driver.quit()