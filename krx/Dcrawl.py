from util.UTIL_monkeypatch import no_ssl_verification
import settings.Dpath as cfg

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

from typing import List
import time


class DeepSearchCrawl:
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

    def browse(self, url:str, page_no:int):
        print(cfg.CRAWLER_OPEN)
        self.browser.get(url.format(page_no))

    def set_summary(self):
        print(cfg.CRAWLER_SUMMARY)
        self.browser.find_element(
            by=By.XPATH,
            value=cfg.NEWS_SUMMARY
        ).click()

    def _collect(self, collections:List, collections_if:list, news_num:int) -> List:
        result = list()
        for ct in collections:
            d = self.browser.find_element(
                by=By.XPATH,
                value=ct.format(news_num)
            )
            result.append(d.text)

        for ict in collections_if:
            try:
                d = self.browser.find_element(
                    by=By.XPATH,
                    value=ict.format(news_num)
                )
                result.append(d.text)
            except Exception as e:
                result.append('')
                pass
        return result

    def collect(self):
        print(cfg.CRAWLER_COLLECTING)
        targets = [
            cfg.NEWS_TITLE,
            cfg.NEWS_TYPE,
            cfg.NEWS_TIME,
            cfg.NEWS_SOURCE,
            cfg.NEWS_CONTENT,
        ]
        iftargets = [
            cfg.NEWS_SENTIMENT,
            cfg.NEWS_COMPANY
        ]

        targets_nopic = [
            cfg.NEWS_TITLE_NOPIC,
            cfg.NEWS_TYPE_NOPIC,
            cfg.NEWS_TIME_NOPIC,
            cfg.NEWS_SOURCE_NOPIC,
            cfg.NEWS_CONTENT_NOPIC
        ]
        iftargets_nopic = [
            cfg.NEWS_SENTIMENT_NOPIC,
            cfg.NEWS_COMPANY_NOPIC
        ]
        column = ['title', 'type', 'time', 'source', 'content', 'sentiment', 'company']

        df = list()
        for news_no in range(2, 11):
            try:
                # IF CARD NEWS HAS PICTURES
                d = self._collect(
                    collections=targets,
                    collections_if=iftargets,
                    news_num=news_no
                )
            except Exception as e:
                # IF CARD NEWS HAS NO PICTURES
                d = self._collect(
                    collections=targets_nopic,
                    collections_if=iftargets_nopic,
                    news_num=news_no
                )
            print(d)
            df.append(d)
        return pd.DataFrame(df, columns=column)

    def run(self, page_number:int):
        # WAIT FOR THE BROWSER TO TURN ON
        self.browse(cfg.DeepSearch_URL, page_number)
        time.sleep(2)

        # SET SHOW_CONTENT_SUMMARY > TRUE
        self.set_summary()
        time.sleep(2)

        input()
        # COLLECT DATA
        r = self.collect()
        return r


if __name__ == "__main__":
    with no_ssl_verification():
        ds = DeepSearchCrawl()
        r = ds.run(2)

