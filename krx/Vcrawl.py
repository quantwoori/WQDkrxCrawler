from util.UTIL_monkeypatch import no_ssl_verification
import settings.Vpath as cfg

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import random
import time


class VixCrawl:
    def __init__(self):
        # INITIALIZE SELENIUM
        chrome = webdriver.ChromeOptions()
        chrome.add_experimental_option(
            'useAutomationExtension',
            False
        )
        # OPEN CHROME BROWSER
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome
        )

    def browse(self, url:str):
        print()
        self.browser.get(url)

    def set_historical(self):
        time.sleep(2)  # WAIT FOR PAGE OPEN
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.BUTTON_HISTORICAL
        ).click()
        time.sleep(1)
        # Enable Multiple Graph
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.BUTTON_MULTIPLE
        ).click()

    def add_date(self):
        time.sleep(1)
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.BUTTON_ADD_DATES
        ).click()
        time.sleep(0.1)
        dt = self.browser.find_element(
            by=By.XPATH,
            value=cfg.TEXT_DATE
        ).text
        print(cfg.MSG_ADD_DATE.format(dt))

    def download(self):
        time.sleep(0.1)
        print(cfg.MSG_HIDDENOPEN)
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.BUTTON_HIDDEN
        ).click()
        time.sleep(0.2)
        print(cfg.MSG_DOWNLOAD)
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.BUTTON_HIDDEN_DOWNLOAD
        ).click()

    def run(self):
        print(cfg.MSG_START)
        self.browse(cfg.URL_VIX)

        print(cfg.MSG_SETTING_ENV)
        self.set_historical()

        rest_count = 0
        for i in range(4869):
            self.add_date()
            rest_count += 1

            if rest_count % 103 == 0:
                rest_time = int(random.randint(80, 270))
                print(f"resting {rest_time}. avoid detection")
                time.sleep(rest_time)


if __name__ == "__main__":
    with no_ssl_verification():
        ds = VixCrawl()
        ds.run()
