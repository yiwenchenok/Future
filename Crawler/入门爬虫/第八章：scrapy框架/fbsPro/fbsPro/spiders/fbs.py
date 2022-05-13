# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fbsPro.items import FbsproItem
from scrapy_redis.spiders import RedisCrawlSpider
class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'sun'

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            new_num = tr.xpath('./td[1]/text()').extract_first()
            new_title = tr.xpath('./td[2]/a[2]/@title').extract_first()

            item = FbsproItem()
            item['title'] = new_title
            item['new_num'] = new_num


            yield item


