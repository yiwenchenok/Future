## 安装scrapy
pip install scrapy
##项目初始化
```angular2html
1.初始化项目
#                   项目名
scrapy startproject SinaNews
2.新建爬虫任务
cd SinaNews
#                任务名    域名
scrapy genspider sina sina.com.cn
#创建后会在spiders生成一个文件：任务名.py,熟悉的话自己写genspider
```
## items声明需要爬取的字段
```angular2html
class FirstspiderItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
```

## spider写爬虫任务
```angular2html
def parse(self, response):
    quotes = response.xpath('//div[@class="quote"]')  #获取一页里面所有quote
    for quote in quotes:
        item = FirstspiderItem()
        item['text'] = quote.xpath('.//span[@class="text"]/text()').extract_first().strip('“|”') #获取第一个元素
        item['author'] = quote.xpath('.//small[@class="author"]/text()').extract_first()
        item['tags'] = quote.xpath('.//a[@class="tag"]/text()').extract() #获取所有的元素
        yield item  #阻塞的状态

    #找下一页的链接
    next = response.xpath("//li[@class='next']/a/@href").extract_first() #/page/4/

    #方法1
    # if next:
    #     next_url = 'http://quotes.toscrape.com' + next
    #     yield scrapy.Request(next_url,callback=self.parse)  #回调函数，继续交给parse去解析,默认回调自己

    #方法2：
    if next:
        yield scrapy.Request(response.urljoin(next))
```
urljoin: 类似于urlib中urljoin
from urllib.parse import urljoin
urljoin('要添加的域名', url)

##调用任务
```angular2html
scrapy crawl 任务名 -o 输出文件
scrapy crawl quotes -o q.csv
scrapy crawl quotes -o q.json
#会在项目根目录下生成一个q.csv或者q.json
```



#  1.初始化项目

scrapy startproject LiePin

## 2.新建一个任务
```angular2html
cd LiePin
#                任务名    域名
scrapy genspider liepin liepin.com
spiders更改一下起始路由
start_urls = ['https://www.liepin.com/zhaopin/?key=python']
settings.py改下robots协议
ROBOTSTXT_OBEY = False
```

## 3.items申明要爬取的字段
```angular2html
class LiepinItem(scrapy.Item):
    title = scrapy.Field() #岗位名
    money = scrapy.Field() #待遇
    addr = scrapy.Field() #工作地点
    edu = scrapy.Field() # 学历要求
    age = scrapy.Field() #工作经验
    link = scrapy.Field() #岗位链接
    company = scrapy.Field() # 公司名称
```
# 4.settings中打开pipline
```angular2html
ITEM_PIPELINES = {
   'LiePin.pipelines.LiepinPipeline': 300,
}
```
# 5.写爬虫逻辑
略

## 6.调用
scrapy crawl liepin -o liepin.csv
```angular2html
from scrapy import cmdline
#默认的数据存储
cmdline.execute('scrapy crawl liepin -o liepin.csv'.split(' '))

#调用pipline的存储方式，必须打开settings.py中的ITEM_PIPELINES
cmdline.execute('scrapy crawl liepin'.split(' '))
```


