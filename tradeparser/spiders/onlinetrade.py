import scrapy
from scrapy.http import HtmlResponse
from tradeparser.items import TradeparserItem
from scrapy.loader import ItemLoader


class OnlinetradeSpider(scrapy.Spider):
    name = 'onlinetrade'
    allowed_domains = ['onlinetrade.ru']

    def __init__(self, search):
        super(OnlinetradeSpider, self).__init__()
        self.start_urls = [
            f'https://www.onlinetrade.ru/sitesearch.html?query={search}']

    def parse(self, response: HtmlResponse):
        links = response.xpath(
            "//a[contains(@class, 'item__name')]/@href").getall()
        for link in links:
            print(link)
            yield response.follow(link, callback=self.parse_item)
        print(links)
        print(len(links))
        pass

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=TradeparserItem(), response=response)
        loader.add_xpath(
            "photos", "//img[contains(@class, 'Image')]/@src | "
                      "//img[contains(@id, 'bigImage')]/@src")
        loader.add_xpath("title", "//h1[contains(@itemprop, 'name')]/text()")
        print()
        yield loader.load_item()
        # item = TradeparserItem()
        # item["title"] = response.xpath(
        #     "//h1[contains(@itemprop, 'name')]/text()").get()
        # item["photos"] = response.xpath(
        #     "//img[contains(@class, 'Image')]/@src "
        #     "| //img[contains(@id, 'bigImage')]/@src").getall()
        # yield item
