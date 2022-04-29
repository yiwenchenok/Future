import pprint

from lxml import etree
if __name__ == "__main__":
    tree=etree.parse('./test.html')
    # r = tree.xpath('/html/head/title')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div[@class="song"]/p[3]')
    # r = tree.xpath('//div[@class="tang"]/ul/li[7]/text()')[0]
    # r = tree.xpath('//div[@class="tang"]/ul/li[7]//text()')[0]
    r = tree.xpath('//div[@class="tang"]/ul/li[1]/a/@href')[0]
    print(r)


