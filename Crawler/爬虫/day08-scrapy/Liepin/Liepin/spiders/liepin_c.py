import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LiepinItem

class LiepinCSpider(CrawlSpider):
    name = 'liepin_c'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@title="下一页"]/a'), callback='parse_start_url', follow=True),
    )

    def parse_start_url(self, response, **kwargs):
        joblist = response.xpath('//div[@class="job-detail-box"]')
        for job in joblist:
            item = LiepinItem()
            item["title"] = job.xpath('.//div[@class="ellipsis-1"]/text()').extract_first().strip()
            item["link"] = job.xpath('.//a/@href').extract_first()
            item["company"] = job.xpath('.//div[@class="job-company-info-box"]//span[1]/text()').extract_first()
            item["money"] = job.xpath('.//span[@class="job-salary"]/text()').extract_first()
            item["addr"] = job.xpath('.//span[@class="ellipsis-1"]/text()').extract_first()
            edu_age = job.xpath('.//span[@class="labels-tag"]/text()').extract()
            item['age'] = edu_age[0]
            item['edu'] = edu_age[1]
            yield item
