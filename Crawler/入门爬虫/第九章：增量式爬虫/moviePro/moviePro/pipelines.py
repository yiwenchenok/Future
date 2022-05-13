# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from redis import Redis
class MovieproPipeline(object):
    conn = None
    def open_spider(self,spider):
        self.conn = spider.conn
    def process_item(self, item, spider):
        dic = {
            'name':item['name'],
            'desc':item['desc']
        }
        # print(dic)
        self.conn.lpush('movieData',dic)
        return item
