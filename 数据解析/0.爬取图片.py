import requests
import pprint
import json

if __name__ == "__main__":
    #如何爬取图片数据
    url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F1115%2F101021113337%2F211010113337-6-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1652878868&t=42fb46bb3cba200277ed9ec27385a6fc'
    #content返回的是二进制形式的图片数据
    # text（字符串） content（二进制）json() (对象)
    img_data = requests.get(url=url).content
    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)