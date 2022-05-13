# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SunproPipeline(object):
    def process_item(self, item, spider):
        #如何判定item的类型
        #将数据写入数据库时，如何保证数据的一致性
        if item.__class__.__name__ == 'DetailItem':
            print(item['new_id'],item['content'])
            pass
        else:
            print(item['new_num'],item['title'])
        return item
