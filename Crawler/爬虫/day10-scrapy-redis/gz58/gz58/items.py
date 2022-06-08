# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Gz58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 分类
    name = scrapy.Field()  # 职位名称
    job_salary = scrapy.Field()  # 薪资
    comp_name = scrapy.Field()  # 公司名称
