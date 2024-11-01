import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.env import Environment

env = Environment()


class XhsWeb:

    def __init__(self, env):
        self.driver = env.driver
        self.config = env.config

    def send_sms_code(self, phone):
        self.set_values(env.config.xpath_phone_input, phone)
        self.click(env.config.xpath_sms_code_sender)

    def phone_login(self, sms_code):
        # set sms code
        self.set_values(env.config.xpath_sms_code_input, sms_code)
        # 登录
        self.click(env.config.xpath_login_button)

    def open(self, url):
        self.driver.get(url)
        time.sleep(env.config.sleep_medium_time)

    def quit(self):
        self.driver.quit()
        sys.exit(0)

    def start_publishing(self):
        self.open(env.config.xhs_publish_url)
        time.sleep(env.config.sleep_medium_time)
        self.click(env.config.xpath_start_publishing)
        # self.switch_to_publishing_picture()

    def switch_to_publishing_picture(self):
        self.click(env.config.xpath_tab_pics)

    def publish_video(self, video_local_path):
        self.click(env.config.xpath_upload_video_button)
        time.sleep(self.config.sleep_long_time)

    def publish_pictures(self, pics):
        self.switch_to_publishing_picture()
        self.set_values(env.config.xpath_upload_video_button, pics)
        time.sleep(self.config.sleep_long_time)
        self.click(env.config.xpath_publish_button)

    def click(self, xpath):
        try:
            WebDriverWait(self.driver, env.config.sleep_short_time, 0.2).until(
                lambda x: x.find_element(By.XPATH, xpath)).click()
        except Exception as e:
            env.logger.error(e)

    def set_values(self, xpath, values):
        try:
            WebDriverWait(self.driver, env.config.sleep_short_time, 0.2).until(
                lambda x: x.find_element(By.XPATH, xpath)).send_keys(values)
        except Exception as e:
            env.logger.error(e)
