from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def search_dates(s_date:datetime, e_date:datetime):
    result = list()
    result.append(s_date)
    d = datetime(s_date.year, s_date.month, 1)
    while d < e_date:
        d += relativedelta(months=1)
        result.append(d)
    return result
