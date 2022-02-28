from settings.Sdt import search_dates
from krx.Xcrawl import KRXIndexComposite

from datetime import datetime
from util.UTIL_monkeypatch import no_ssl_verification


with no_ssl_verification():
    d0 = datetime(2010, 1, 1)
    d1 = datetime(2022, 2, 28)
    ds = search_dates(d0, d1)

    krx = KRXIndexComposite(srch_key='코스피 소형주', date=ds)
    