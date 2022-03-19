from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from tradeparser import settings
from tradeparser.spiders.onlinetrade import OnlinetradeSpider
from urllib.parse import quote_plus


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    search = quote_plus("материнская плата asus".encode("cp1251"))
    print(search)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(OnlinetradeSpider, search=search)
    process.start()
