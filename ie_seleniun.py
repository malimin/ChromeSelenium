#-*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/3/24

from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import random
import time


def get_snap(driver):
    # 保存截屏图片，到本地
    driver.save_screenshot('C:/code/ChromeSelenium/full_snap.png')
    # 打开本地图片，获取并返回图片对象
    page_snap_obj = Image.open('//full_snap.png')
    return page_snap_obj


def get_image(driver):
    # 从网页获取图片的大小及位置
    # img = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[2]/div[1]/div[2]/div[1]/a[2]/div[1]')
    img = driver.find_element_by_id("svcodeBack")
    time.sleep(2)
    # 获取img尺寸
    location = img.location
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    # 从保存到本地的截屏，切取图片
    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    # 返回图片对象
    # print(left, top, right, bottom)
    return image_obj


def get_distance(image1, image2):
    start = 57
    threhold = 60
    #  对比两张图片，查找缺口位置
    for i in range(start, image1.size[0]):
        for j in range(image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return i - 7
    return i - 7

def get_tracks(distance):
    # 模拟人手动滑动，先滑过一点，最后再反着滑动回来
    distance += 20
    v = 0
    t = 0.2
    forward_tracks = []

    current = 0
    mid = distance * 3 / 5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3

        s = v * t + 0.5 * a * (t ** 2)
        v = v + a * t
        current += s
        forward_tracks.append(round(s))

    # 反着滑动到准确位置
    back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20

    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}
    # track = []
    # current = 0
    # mid = distance*3/4
    # t = random.randint(2,3)/10
    # v = 0
    # while  current < distance:
    #     if current < mid :
    #         a = 2
    #     else:
    #         a = -3
    #     v0 = v
    #     v = v0 + a * t
    #     move = v0*t + 1/2 * a * t *t
    #     current += move
    #     track.append(round(move))
    # return track

def crack(driver):
    # 获取没有缺口的图片
    image1 = get_image(driver)
    time.sleep(0.5)
    driver.find_element_by_id("customerId").send_keys("1")
    # driver.find_element_by_id("customerId").click()
    # 将按钮移动到最后，得到有缺口的图片
    # button = driver.find_element_by_css_selector('body > div.gt_holder.gt_popup.gt_show > div.gt_popup_wrap > div.gt_popup_box > div.gt_slider > div.gt_slider_knob.gt_show')
    #button = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[2]/div[2]/div[2]')
    button = driver.find_element_by_css_selector('body > div.login_content1 > form#form1 > div.login_cont > ul > li:nth-child(3) > div#slideVerifyImgCode > div.svcode-div > div.svcode-con > div.svcode-btn > div[class="svcode-btn-img svcode-btn-m"]')
    # button = driver.find_element_by_class("svcode-btn-img svcode-btn-m")
    print(button)
    # print(driver.location(button))
    # return
    time.sleep(1)
    ActionChains(driver).click_and_hold(button).perform()
    time.sleep(0.58)
    ActionChains(driver).move_by_offset(xoffset=10, yoffset=0).perform()
    time.sleep(0.35)
    image2 = get_image(driver)
    time.sleep(0.35)
    return
    # 对比两种图片的像素点，找出位移
    distance = get_distance(image1, image2)
    time.sleep(0.23)
    # 返回起始位置
    ActionChains(driver).move_by_offset(xoffset=-198, yoffset=0).perform()
    time.sleep(0.5)
    # 模拟人的行为习惯，根据总位移得到行为轨迹
    track_list = get_tracks(distance+3)
    print(track_list)
    # 按照行动轨迹先正向滑动，后反滑动
    for track in track_list:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    imitate = ActionChains(driver).move_by_offset(xoffset=-1,yoffset=0)
    time.sleep(0.015)
    imitate.perform()
    time.sleep(random.randint(6,10)/10)
    imitate.perform()
    time.sleep(0.04)
    imitate.perform()
    time.sleep(0.012)
    imitate.perform()
    time.sleep(0.019)
    imitate.perform()
    time.sleep(0.033)
    # time.sleep(0.9)
    # # for track in tracks['forward_tracks']:
    # #     ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    # # time.sleep(0.9)
    # # 开始反向滑动
    # for back_track in tracks['back_tracks']:
    #     ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()
    # time.sleep(0.5)
    # # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
    # ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    # time.sleep(0.3)
    # rand = random.randint(2,4)
    ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
    # time.sleep(0.5)
    # 释放鼠标
    ActionChains(driver).pause(random.randint(6,14)/10).release(button).perform()
    time.sleep(2)


if __name__ == '__main__':

    driver = webdriver.Ie()
    driver.get("https://www.baidu.com")
    time.sleep(2)
    driver.get("https://corporbank.abchina.com/CorporServPlat/QryVersionStartUpAct.do")
    time.sleep(1)
    crack(driver)
    driver.quit()