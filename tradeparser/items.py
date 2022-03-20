# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def get_big_img_url(url):
    return url.replace("/m/", "/b/").replace("/s/", "/b/")


class TradeparserItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(get_big_img_url))
    _id = scrapy.Field()
