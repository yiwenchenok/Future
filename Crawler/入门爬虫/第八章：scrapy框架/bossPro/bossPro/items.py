# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossproItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_desc = scrapy.Field()
    # pass
