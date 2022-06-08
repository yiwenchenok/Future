# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import uuid
import re

class SinanewsPipeline:
    def process_item(self, item, spider):
        filename = str(uuid.uuid4()).replace("-", "") + ".txt"  # 时间撮，命名空间，随机数，伪随机数保证id唯一性
        save_path = item['subFileName'] + '/' + filename
        content = ""
        if item['content']:
            content = re.sub("[^\u4e00-\u9fa5，。、：；“”]",'',item['content']) #删除非中文的
        with open(save_path,'w',encoding='utf-8') as f:

            f.write(content)
        return item
