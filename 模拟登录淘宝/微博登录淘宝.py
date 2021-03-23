import requests
import time
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from configparser import *
from urllib.parse import quote

username = ''#微博账号 需要先绑定淘宝
password = ''#微博密码
try:
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    # 下一行代码是为了以开发者模式打开chrome
    chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://s.taobao.com/search?q=iPad")
    button = browser.find_element_by_class_name('weibo-login')
    button.click()
    user_name = browser.find_element_by_name('username')
    user_name.clear()
    user_name.send_keys(username)
    time.sleep(1)
    user_keys = browser.find_element_by_name('password')
    user_keys.clear()
    user_keys.send_keys(password) #输入微博密码
    time.sleep(1)
    button = browser.find_element_by_class_name('W_btn_g')
    button.click()
    time.sleep(1)
    cookies = browser.get_cookies()
    ses = requests.Session() # 维持登录状态
    c = requests.cookies.RequestsCookieJar()
    for item in cookies:
        c.set(item["name"],item["value"])
        ses.cookies.update(c)
        ses = requests.Session()
        time.sleep(1)
    print('登录成功')
except:
    print("登录失败")