# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import Gz58Item
from scrapy_redis.spiders import RedisSpider


class GzSpider(RedisSpider):   # 1、修改继承类
    name = 'gz'
    allowed_domains = ['58.com']
    # start_urls = ['http://gz.58.com/job.shtml?']   # 2、修改起始url,  redis_key
    redis_key = "gz:start_keys"     # redis_key,用于在redis 添加起始url
    #todo:    LPUSH gz:start_keys 'http://gz.58.com/job.shtml?'
    def parse(self, response):
        """
        获取所有的职位类型url
        :param response:
        :return:
        """
        # 获取所有title 先获取第1个来爬 a[1]
        positions_list = response.xpath("//div[@id='sidebar-right']//a[1]")
        for i in positions_list:
            title = i.xpath('./text()').extract_first()  # 获取到title
            title = re.sub(r"/", "_", title)
            url = i.xpath("./@href").extract_first()  # 获取url
            gz_url = 'http://gz.58.com' + url
            print(title, gz_url)
            yield scrapy.Request(url=gz_url, callback=self.parse_item,
                                 meta={"title": title})

    def parse_item(self, response):
        """解析职位信息数据"""
        li = response.xpath("//ul[@id='list_con']/li")
        title = response.meta.get("title")
        for i in li:
            item = Gz58Item()
            # 职位名称
            name = i.xpath(".//div[@class='job_name clearfix']/a/span[2]/text()").extract_first()
            # 薪资
            job_salary = i.xpath('.//div[@class="item_con job_title"]/p[@class="job_salary"]').xpath("string(.)").extract_first()
            # 公司名称
            comp_name = i.xpath(".//div[@class='comp_name']/a/@title").extract_first()

            # print(name, job_salary, comp_name)

            item["title"] = title
            item["name"] = name
            item["job_salary"] = job_salary
            item["comp_name"] = comp_name
            yield item

        # 在源码里面中 “next disabled” 没有找到说明还可以获取下一页链接，然后发送请求
        if response.text.find("next disabled") == -1:
            # 获取下一页的链接
            # next_url = response.xpath("//div[@class='pagesout']/a[@class='next']/@href").extract_first()
            next_url = response.xpath(".//a[@class='next']/@href").extract_first()
            if next_url:
                # 发送下一页请求
                yield scrapy.Request(url=next_url, callback=self.parse_item, meta={"title": title})
