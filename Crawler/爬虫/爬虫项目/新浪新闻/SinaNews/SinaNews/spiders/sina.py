import os

import scrapy
from ..items import SinanewsItem




class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']
    def parse(self, response):
        #所有大类的标题和链接
        parentTitles=response.xpath('//div[@id="XX_conts"]//h3/a/text()').extract()
        parentUrls=response.xpath('//div[@id="XX_conts"]//h3/a/@href').extract()
        #所有子类的标题和链接
        subTitles=response.xpath('//div[@id="XX_conts"]//ul/li/a/text()').extract()
        subUrls=response.xpath('//div[@id="XX_conts"]//ul/li/a/@href').extract()
        #遍历所有大类
        for i in range(len(parentTitles)):
            save_path='data/'
            parentFileName=os.path.join(save_path, parentTitles[i])
            if not os.path.exists(parentFileName):
                os.makedirs(parentFileName) #如果目录不存在，则创建目录
            #遍历所有小类
            for j in range(len(subTitles)):
                item=SinanewsItem()
                #保存大标题的信息
                item["parentTitle"]=parentTitles[i]
                item["parentUrl"]=parentUrls[i]
                #保存小类的链接，如果链接跟大类同则表示是子类
                flag=subUrls[j].replace('https','http').startswith(item["parentUrl"])
                if flag:
                    subFileName=os.path.join(parentFileName,subTitles[j])
                    if not os.path.exists(subFileName):
                        os.makedirs(subFileName)
                    item["subTitle"] = subTitles[j]
                    item["subUrl"] = subUrls[j]
                    item["subFileName"] = subFileName
                    yield scrapy.Request(item['subUrl'],meta={'item_1':item}, callback=self.second_parse)


    def second_parse(self,response):
        """获取小标题界面的a链接"""
        item_1 = response.meta.get('item_1')
        #todo:获取当前页面上的所有a链接
        sonurls = response.xpath('//a/@href').extract()
        for i in range(len(sonurls)):
            #检查是否以.shtml结尾，以大类开头
            flag = sonurls[i].endswith(".shtml") and sonurls[i].replace('https','http').startswith(item_1['parentUrl'])
            if flag:
                item = SinanewsItem()
                item['parentTitle'] = item_1['parentTitle']
                item['parentUrl'] = item_1['parentUrl']
                item['subTitle'] = item_1['subTitle']
                item['subUrl'] = item_1['subUrl']
                item['subFileName'] = item_1['subFileName']
                item['sonUrl'] = sonurls[i]  #最终的子新闻的链接页面
                yield scrapy.Request(item['sonUrl'] , meta={'item_2': item}, callback=self.detail_parse)

    def detail_parse(self,response):
        """解析最终的链接页面"""
        item_2 = response.meta.get('item_2')
        head = response.xpath('//h1[contains(@class,"main-title") or contains(@class,"article-title") ]').extract_first()
        content = response.xpath("//div[contains(@class,'article-content-left') or contains(@class,'article')]").xpath('string(.)').extract_first()
        item = SinanewsItem()
        item['parentTitle'] = item_2['parentTitle']
        item['parentUrl'] = item_2['parentUrl']
        item['subTitle'] = item_2['subTitle']
        item['subUrl'] = item_2['subUrl']
        item['subFileName'] = item_2['subFileName']
        item['sonUrl'] = item_2['sonUrl']
        item['head'] = head
        item['content'] = content

        yield item





