# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem

#需求：爬取sun网站中的编号，新闻标题，新闻内容，标号
class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    #链接提取器：根据指定规则（allow="正则"）进行指定链接的提取
    link = LinkExtractor(allow=r'type=4&page=\d+')
    link_detail = LinkExtractor(allow=r'question/\d+/\d+\.shtml')
    rules = (
        #规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        Rule(link, callback='parse_item', follow=True),
        #follow=True：可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的页面中
        Rule(link_detail,callback='parse_detail')
    )
    #http://wz.sun0769.com/html/question/201907/421001.shtml
    #http://wz.sun0769.com/html/question/201907/420987.shtml

    #解析新闻编号和新闻的标题
    #如下两个解析方法中是不可以实现请求传参！
    #如法将两个解析方法解析的数据存储到同一个item中，可以以此存储到两个item
    def parse_item(self, response):
        #注意：xpath表达式中不可以出现tbody标签
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            new_num = tr.xpath('./td[1]/text()').extract_first()
            new_title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num

            yield item

    #解析新闻内容和新闻编号
    def parse_detail(self,response):
        new_id = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        new_content = response.xpath('/html/body/div[9]/table[2]//tr[1]//text()').extract()
        new_content = ''.join(new_content)

        # print(new_id,new_content)
        item = DetailItem()
        item['content'] = new_content
        item['new_id'] = new_id

        yield item