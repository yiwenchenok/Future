import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FirstspiderItem

class QuotesCSpider(CrawlSpider):
    name = 'quotes_c'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'/page/\d+'), callback='parse_item', follow=True),  #会有太多的重复
        # Rule(LinkExtractor(allow=r'http://quotes.toscrape.com/page/\d+'), callback='parse_item', follow=True), #正确的写法

        #推荐写法
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'), callback='parse_start_url', follow=True),  #回调函数需要调用parse_start_url,开始页页抓取内容
    )

    def parse_start_url(self, response, **kwargs):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = FirstspiderItem()
            item["text"] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            item["author"] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item["tags"] = quote.xpath('.//a[@class="tag"]/text()').extract()
            yield  item
