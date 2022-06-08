# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    money = scrapy.Field()
    addr = scrapy.Field()
    edu = scrapy.Field()
    age = scrapy.Field()
    link = scrapy.Field()
    company = scrapy.Field()

