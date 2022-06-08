import scrapy
import re
from ..items import Gz58Item

class GzSpider(scrapy.Spider):
    name = 'gz'
    allowed_domains = ['58.com']

    start_urls = ['https://gz.58.com/job.shtml']

    def parse(self, response):
        #获取职位title  分类
        # positions_list = response.xpath("//div[@id='sidebar-right']//a[1]")
        print('开始获取标题和链接')
        positions_list = response.xpath("//div[@id='sidebar-right']//a")
        for i in positions_list:
            title = i.xpath('./text()').extract_first()
            title = re.sub(r'/','_',title)
            print(title)
            url = 'https://gz.58.com'+i.xpath('./@href').extract_first()
            print(url)
            yield scrapy.Request(url=url,callback=self.parse_item,meta={'title':title})

    def parse_item(self, response):
        print('开始获取详情页标题和链接')
        li = response.xpath('//ul[@id="list_con"]/li')
        title = response.meta.get("title")
        for i in li:
            item = Gz58Item()
            item['title'] = title
            item['name'] = i.xpath('.//div[@class="job_name clearfix"]/a/span[2]/text()').extract_first()
            item['job_salary'] = i.xpath('.//div[@class="item_con job_title"]/p[@class="job_salary"]').xpath('string(.)').extract_first()
            item['comp_name'] = i.xpath('.//div[@class="comp_name"]/a/@title').extract_first()
            print('保存成功')
            yield item
        next_url = response.xpath("//a[@class='next']/@href").extract_first()

        if response.text.find('next disabled') == -1:  #如果可以获取到下一页链接
            if next_url:
                print("下一页")
                yield scrapy.Request(next_url,callback=self.parse_item,meta={'title':title},)


