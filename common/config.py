import configparser
import os.path
import sys
from pathlib import Path

from fake_useragent import UserAgent
from selenium.webdriver.firefox.options import Options


def get_project_dir():
    current_dir = Path(__file__)
    return [p for p in current_dir.parents if p.parts[-1] == '24-insta-rpa'][0]


def yt_options(path):
    return {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }


class CrawlerConfig(object):

    def __init__(self):
        config_file = f'{get_project_dir()}/common/config.ini'
        if not os.path.isfile(config_file):
            print(f'config file not found: {config_file}')
            sys.exit(0)

        cp = configparser.ConfigParser()
        cp.read(config_file)
        # insta
        self._username = cp.get('insta', 'user_name')
        self._password = cp.get('insta', 'password')
        self._home_url = cp.get('insta', 'host')
        self._vocabulary_url = cp.get('insta', 'author')
        # sleep
        self._short_sleep = cp.get('sleep', 'short')
        self._medium_sleep = cp.get('sleep', 'medium')
        self._long_sleep = cp.get('sleep', 'long')
        # files
        self._log_file = cp.get('file', 'log')
        self._cookie_file = cp.get('file', 'cookie')
        self._db_path = cp.get('file', 'db')
        self._opus_dir = cp.get('file', 'opus_dir')
        # xhs
        self._xhs_phone = cp.get('xhs', 'phone')
        self._xhs_login_url = cp.get('xhs', 'login_url')
        self._xhs_publish_url = cp.get('xhs', 'publish_url')
        #xpath
        self._xpath_phone_input = cp.get('xpath', 'phone_input')
        self._xpath_sms_code_sender = cp.get('xpath', 'sms_code_sender')
        self._xpath_sms_code_input = cp.get('xpath', 'sms_code_input')
        self._xpath_login_button = cp.get('xpath', 'login_button')
        self._xpath_start_publishing = cp.get('xpath', 'start_publishing')
        self._xpath_tab_pics = cp.get('xpath', 'tab_pics')
        self._xpath_upload_video_button  = cp.get('xpath', 'upload_video_button')
        self._xpath_upload_pic_button = cp.get('xpath', 'upload_pic_button')
        self._xpath_publish_button = cp.get('xpath', 'publish_button')

    @property
    def xpath_phone_input(self):
        return self._xpath_phone_input

    @property
    def xpath_sms_code_sender(self):
        return self._xpath_sms_code_sender

    @property
    def xpath_sms_code_input(self):
        return self._xpath_sms_code_input

    @property
    def xpath_login_button(self):
        return self._xpath_login_button

    @property
    def xpath_start_publishing(self):
        return self._xpath_start_publishing

    @property
    def xpath_tab_pics(self):
        return self._xpath_tab_pics

    @property
    def xpath_upload_video_button(self):
        return self._xpath_upload_video_button

    @property
    def xpath_upload_pic_button(self):
        return self._xpath_upload_pic_button

    @property
    def xpath_publish_button(self):
        return self._xpath_publish_button

    @property
    def xhs_phone(self):
        return self._xhs_phone

    @property
    def xhs_login_url(self):
        return self._xhs_login_url

    @property
    def xhs_publish_url(self):
        return self._xhs_publish_url

    @property
    def insta_user_name(self):
        return self._username

    @property
    def insta_password(self):
        return self._password

    @property
    def insta_home_url(self):
        return self._home_url

    def insta_opus_url(self, code):
        return f'https://www.instagram.com/p/{code}/'

    @property
    def insta_vocabulary_url(self):
        return self._vocabulary_url

    @property
    def sleep_short_time(self):
        return int(self._short_sleep)

    @property
    def sleep_medium_time(self):
        return int(self._medium_sleep)

    @property
    def sleep_long_time(self):
        return int(self._long_sleep)

    @property
    def log_file_name(self):
        return f'{get_project_dir()}/{self._log_file}'

    @property
    def cookie_file_name(self):
        return f'{get_project_dir()}/{self._cookie_file}'

    @property
    def db_file_name(self):
        return f'sqlite:////{get_project_dir()}/{self._db_path}'

    @property
    def opus_dir(self):
        return f'{get_project_dir()}/{self._opus_dir}'

    @property
    def driver_options(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument(f'user-agent=={UserAgent().random}')
        # 无界面模式
        # options.add_argument('--headless')
        return options

