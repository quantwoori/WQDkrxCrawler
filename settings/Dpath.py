from settings.Scolors import LColors

# DeepSearch URL
DeepSearch_URL = "https://www.deepsearch.com/analytics/news-room/news?n-p={}"

# DeepSearch XPATH VALUES
NEWS_SUMMARY = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[2]"

NEWS_TITLE = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[1]/span"
NEWS_TYPE = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[2]/span[1]"
NEWS_CONTENT = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[3]/span"
NEWS_SOURCE = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[2]/span[2]"
NEWS_TIME = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[2]/span[3]"
NEWS_SENTIMENT = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[2]/span[4]"
NEWS_COMPANY = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div[2]/div[4]"

NEWS_TITLE_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[1]/span"
NEWS_TYPE_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[2]/span[1]"
NEWS_CONTENT_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[3]/span"
NEWS_SOURCE_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[2]/span[2]"
NEWS_TIME_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[2]/span[3]"
NEWS_SENTIMENT_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[2]/span[4]"
NEWS_COMPANY_NOPIC = "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[{}]/div/div[4]"

# DeepSearch MESSAGE
CRAWLER_OPEN = "[DeepSearch] >>> OPEN URL"
CRAWLER_SUMMARY = "[DeepSearch] >>> OPENING CONTENT SUMMARY"
CRAWLER_COLLECTING = "[DeepSearch] >>> COLLECTING DATA"

