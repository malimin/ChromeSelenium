#-*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/3/13

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# chrome.exe --start-maximized --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=chrome_options)

"""
# 切换frame
driver.switch_to_frame("mainFrame")
# 定位到第一条邮件，并点击勾选
driver.find_element_by_xpath('//*[@id="div_showbefore"]/table[1]/tbody/tr/td[1]/input').click()
# 点击标记下拉菜单
driver.find_element_by_id("markContainer").click()
time.sleep(1)
# 点击为“已读邮件”
# driver.find_element_by_xpath('//*[@id="select_QMMenu__menuitem_read"]').click()
driver.find_element_by_id('select_QMMenu__menuitem_read').click()
"""
# 切换frame
# driver.switch_to_frame("mainFrame")
driver.switch_to.frame("mainFrame")

# cla = driver.find_element_by_xpath('//*[@id="div_showbefore"]/table[1]').get_attribute('class')
# print(cla)
time.sleep(2)
clas = driver.find_elements_by_xpath('//*[@id="div_showbefore"]/table[*]')
for cla in clas:
    c = cla.get_attribute("class")
    print(c)

driver.implicitly_wait(2)

print(driver.title)

# driver.quit()