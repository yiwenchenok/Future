import scrapy
from ..items import FirstspiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = FirstspiderItem()
            item["text"] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            item["author"] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item["tags"] = quote.xpath('.//a[@class="tag"]/text()').extract()
            yield  item

        next = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next:
            # next_url = 'http://quotes.toscrape.com' + next
            # yield  scrapy.Request(next_url,callback=self.parse) #callback表示回调，默认是自己
            yield scrapy.Request(response.urljoin(next),callback=self.parse) #效果同上




