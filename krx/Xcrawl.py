from util.UTIL_monkeypatch import no_ssl_verification
import settings.Spath as cfg
from settings.Sdt import search_dates

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta
from os.path import isfile, join
from os import listdir
import time
import os


class KRXIndexComposite:
    def __init__(self, srch_key:str, date:[datetime]):
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
        if len(date) > 1:
            # MULTI DATES
            print(cfg.CRAWLER_CONFIGURE_MULTI)
            self.run_multi(srch_key, date)
        else:
            # SINGLE DATE
            print(cfg.CRAWLER_CONFIGURE_SINGLE)
            self.run(srch_key, date[0])

    def browse(self, url:str):
        print(cfg.CRAWLER_OPEN)
        self.browser.get(url)

    def input_hidden_key(self, keyword:str):
        print(cfg.CRAWLER_SRCH_HIDDEN)
        # HIDDEN WINDOW PROCESSING
        hid = self.browser.find_element(
            by=By.XPATH,
            value=cfg.HIDDEN_BLANK
        )
        time.sleep(0.1)
        hid.clear()
        time.sleep(0.1)
        hid.send_keys(keyword)

        time.sleep(0.1)
        hid_src = self.browser.find_element(
            by=By.XPATH,
            value=cfg.HIDDEN_BUTTON
        )
        hid_src.click()

        time.sleep(0.5)
        hid_val = self.browser.find_element(
            by=By.XPATH,
            value=cfg.HIDDEN_VAL
        )
        hid_val.click()

    def input_srch_key(self, keyword:str):
        print(cfg.CRAWLER_SRCH_KEY)
        time.sleep(0.5)
        # INPUT SEARCH KEYWORD
        inp = self.browser.find_element(
            by=By.XPATH,
            value=cfg.SRCH_BLANK
        )
        inp.click()
        time.sleep(0.2)
        inp.send_keys(keyword)
        time.sleep(0.2)

        clc = self.browser.find_element(
            by=By.XPATH,
            value=cfg.SRCH_BUTTON
        )
        clc.click()
        time.sleep(0.5)

    def input_date(self, dt:datetime, dfmt='%Y%m%d'):
        print(cfg.CRAWLER_SRCH_DATE.format(dt.strftime(dfmt)))
        time.sleep(0.5)
        # INPUT SEARCH DATETIME
        inp = self.browser.find_element(
            by=By.XPATH,
            value=cfg.SRCH_DATE
        )
        inp.clear()
        time.sleep(0.5)

        inp.send_keys(dt.strftime(dfmt))
        time.sleep(0.5)

        inp.submit()
        time.sleep(1)

    def search_start(self):
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.SRCH_MAIN
        ).click()
        time.sleep(5)

    def download_srch(self):
        # ENTER FILE TYPE SELECTION
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.DOWNLOAD0
        ).click()
        time.sleep(1)

        # SELECT CSV & DOWNLOAD
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.DOWNLOAD1
        ).click()
        print(cfg.CRAWLER_SRCH_DOWNLOAD)

    def process_download_files(self, search_date:datetime, org_path:str='C:/Users/wooriam/Downloads',
                               new_path:str='C:/Users/Wooriam/PycharmProjects/krxCrawler/download', dfmt='%Y%m%d'):
        time.sleep(5)
        print(cfg.CRAWLER_SRCH_PROC)
        dt = search_date.strftime(dfmt)
        f = [f for f in listdir(org_path)
             if isfile(join(org_path, f))]
        f = [file for file in f if file[:4] == 'data']  # What I've just downloaded
        for file in f:
            os.rename(f"{org_path}/{file}", f"{new_path}/{dt}.csv")

    def nodata_handle(self):
        print(cfg.CRAWLER_SRCH_ERR1)
        time.sleep(1)
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.ERR_HANDLE
        ).click()
        time.sleep(0.5)

    def run(self, keyword:str, date:datetime, dfmt='%Y%m%d'):
        self.browse(cfg.KRX_URL)
        # INSERT SEARCH KEYS
        self.input_srch_key(keyword)
        self.input_hidden_key(keyword)

        # INSERT SEARCH DATES
        self.input_date(date)

        # MAIN SEARCH STARTS
        add_date, err_count = 0, 0
        self.search_start()
        while True:
            try:
                self.download_srch()
                self.process_download_files(date)
            except Exception as e:
                err_count += 1
                if err_count >= 31:
                    print(cfg.CRAWLER_SRCH_ERR4)

                print(cfg.CRAWLER_SRCH_ERR0.format(date.strftime(dfmt)))
                self.nodata_handle()
                print(cfg.CRAWLER_SRCH_ERR2)
                add_date += 1
                d = date + timedelta(days=add_date)

                self.input_date(d)
                self.search_start()
            else:
                # INITIALIZE THE ERROR HANDLE VALUE
                print(cfg.CRAWLER_SRCH_ERR3)
                add_date = 0
                break

    def run_multi(self, keyword:str, dates:[datetime], dfmt='%Y%m%d'):
        self.browse(cfg.KRX_URL)
        self.input_srch_key(keyword)
        self.input_hidden_key(keyword)

        for dt in dates:
            self.input_date(dt)
            add_date, err_count = 0, 0
            self.search_start()
            while True:
                try:
                    self.download_srch()
                    self.process_download_files(dt)
                except Exception as e:
                    err_count += 1
                    if err_count >= 31:
                        print(cfg.CRAWLER_SRCH_ERR4)
                        break

                    print(cfg.CRAWLER_SRCH_ERR0.format(dt.strftime(dfmt)))
                    self.nodata_handle()
                    print(cfg.CRAWLER_SRCH_ERR2)
                    add_date += 1
                    d = dt + timedelta(days=add_date)

                    self.input_date(d)
                    self.search_start()
                else:
                    # INITIALIZE THE ERROR HANDLE VALUE
                    print(cfg.CRAWLER_SRCH_ERR3)
                    add_date, err_count = 0, 0
                    break


if __name__ == '__main__':
    with no_ssl_verification():
        d0 = datetime(2022, 5, 1)
        d1 = datetime(2022, 5, 28)
        ds = search_dates(d0, d1)
        krx = KRXIndexComposite(
            srch_key='코스피 200',
            date=ds
        )
