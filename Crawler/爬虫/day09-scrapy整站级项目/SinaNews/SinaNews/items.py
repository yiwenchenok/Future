# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parentTitle = scrapy.Field()   #新闻大标题
    subTitle = scrapy.Field()   #新闻小类标题
    parentUrl = scrapy.Field()   #新闻大标题链接
    subUrl = scrapy.Field()   #新闻小类标题链接

    #新闻小类存储路径
    subFileName = scrapy.Field()

    #小类中子新闻的链接，标题，内容
    sonUrl = scrapy.Field()
    head = scrapy.Field()  #标题
    content = scrapy.Field() #内容

