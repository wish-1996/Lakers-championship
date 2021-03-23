from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Login:
    def __init__(self, username, password):
        """
        初始化浏览器配置和登录信息
        """
        self.url = 'https://login.taobao.com/member/login.jhtml'
        # 初始化浏览器选项
        options = webdriver.ChromeOptions()
        # 禁止加载图片
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 加载浏览器选项
        self.browser = webdriver.Chrome(options=options)
        # 设置显式等待时间40s
        self.wait = WebDriverWait(self.browser, 40)
        self.username = username # 用户名
        self.password = password # 密码

    def original(self):
        """
        直接使用淘宝账号登录

        :return: None
        """
        self.browser.get(url=self.url)
        try:
            input_username = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-loginid > input'
            )))
            input_password = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-password > input'
            )))
            # 等待滑块按钮加载
            div = self.wait.until(EC.presence_of_element_located((
                By.ID, 'nc_1__bg'
            )))
            input_username.send_keys(self.username)
            input_password.send_keys(self.password)
            # 休眠2s，等待滑块按钮加载
            time.sleep(2)
            # 点击并按住滑块
            ActionChains(self.browser).click_and_hold(div).perform()
            # 移动滑块
            ActionChains(self.browser).move_by_offset(xoffset=300, yoffset=0).perform()
            # 等待验证通过
            self.wait.until(EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'
            ))
            # 登录
            input_password.send_keys(Keys.ENTER)
            print('Successful !')
        except TimeoutException as e:
            print('Error:', e.args)
            self.original()

