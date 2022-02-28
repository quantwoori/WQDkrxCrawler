from settings.Scolors import LColors

# KRX URL
KRX_URL = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010106"

# KRX XPATH VALUES
SRCH_BLANK = '//*[@id="tboxindIdx_finder_equidx0_0"]'
SRCH_BUTTON = '//*[@id="btnindIdx_finder_equidx0_0"]'

HIDDEN_BLANK = '/html/body/div[2]/section[2]/section/section/div/div/div[3]/div[2]/div/form/div[2]/input[1]'
HIDDEN_BUTTON = '/html/body/div[2]/section[2]/section/section/div/div/div[3]/div[2]/div/form/div[2]/a'
HIDDEN_VAL = '/html/body/div[2]/section[2]/section/section/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'

SRCH_DATE = '//*[@id="trdDd"]'
SRCH_MAIN = '//*[@id="jsSearchButton"]'

DOWNLOAD0 = '//*[@id="MDCSTAT006_FORM"]/div[2]/div[1]/p[2]/button[2]'
DOWNLOAD1 = '/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div[2]/div[2]/div/div[2]/a'

ERR_HANDLE = '/html/body/div[4]/div[3]/div/button'

# CRAWLER MESSAGE
CRAWLER_OPEN = "[KRX CRAWL] >>> OPEN URL"
CRAWLER_CONFIGURE_SINGLE = "[KRX CRAWL] >>> SEARCHING SINGLE DATE"
CRAWLER_CONFIGURE_MULTI = "[KRX CRAWL] >>> SEARCHING MULTIPLE DATES"
CRAWLER_SRCH_KEY = "[KRX CRAWL] >>> INPUT SEARCH KEYWORD"
CRAWLER_SRCH_DATE = "[KRX CRAWL] >>> INPUT SEARCH DATE {}"
CRAWLER_SRCH_HIDDEN = "[KRX CRAWL] >>> PROCESSING HIDDEN WINDOW"
CRAWLER_SRCH_DOWNLOAD = f"{LColors.OKCYAN}[KRX CRAWL] >>> DOWNLOADING RESULTS{LColors.ENDC}"
CRAWLER_SRCH_PROC = "[KRX CRAWL] >>> RENAME, RELOCATE RESULTS"

CRAWLER_SRCH_ERR0 = f"{LColors.WARNING}[KRX CRAWL] >>> RESULT DOES NOT EXISTS{LColors.ENDC}"
CRAWLER_SRCH_ERR1 = f"{LColors.WARNING}[KRX CRAWL] >>> ERROR HANDLE >>> CLOSE ERR WINDOW{LColors.ENDC}"
CRAWLER_SRCH_ERR2 = f"{LColors.WARNING}[KRX CRAWL] >>> ERROR HANDLE >>> +1 DATE SEARCH{LColors.ENDC}"
CRAWLER_SRCH_ERR3 = f"{LColors.OKGREEN}[KRX CRAWL] >>> ERROR HANDLE >>> INITIALIZE VALUE{LColors.ENDC}"
CRAWLER_SRCH_ERR4 = f"{LColors.FAIL}[KRX CRAWL] >>> PANIC >>> SOMETHING REALLY WRONG{LColors.ENDC}"
