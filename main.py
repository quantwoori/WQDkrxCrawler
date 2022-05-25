from settings.Sdt import search_dates
from krx.Xcrawl import KRXIndexComposite

from datetime import datetime
from util.UTIL_monkeypatch import no_ssl_verification


def automate_krx(target_index:str):
    t = datetime.now()
    d0 = datetime(t.year, t.month, 1)
    d1 = datetime(t.year, t.month, 20)
    ds = search_dates(d0, d1)
    # download data
    with no_ssl_verification():
        krx = KRXIndexComposite(
            srch_key=target_index,
            date=ds
        )

