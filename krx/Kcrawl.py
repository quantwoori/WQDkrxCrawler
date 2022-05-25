from util.UTIL_monkeypatch import no_ssl_verification
import requests

# For Google API
from pytrends.request import TrendReq as GoogleTrend

# For NAVER API
from security.key import NAVER


class Google:
    def __init__(self):
        # Class Constant
        # https://forbrains.co.uk/international_tools/earth_timezones?ref=hackernoon.com
        KOR, KORTIME = 'ko-KR', 540
        ENG, ENGTIME = 'en-US', 360

        # Class local modules
        self.mod = GoogleTrend()

    def keyword(self):
        df = self.mod.trending_searches(pn='korea')


class Naver:
    HEADER = {
        "X-Naver-Client-Id": NAVER['access_key'],
        "X-Naver-Client-Secret": NAVER['secret_key'],
        "Content-Type": "application/json"
    }
    URL = "https://openapi.naver.com/v1/datalab/search"

    def __init__(self):
        ...


if __name__ == "__main__":
    with no_ssl_verification():
        g = Google()
        df = g.mod.trending_searches(pn='south_korea')
