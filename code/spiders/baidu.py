#coding:utf-8


from scrapy_plus.core.spider import Spider
from scrapy_plus.http.item import Item


class BaiduSpider(Spider):

    name = "baidu"
    # 子类重写父类的同名属性，提供新的属性值
    start_urls = [
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/"
    ]

    def parse(self, response):
        item = {}
        item['title'] = response.xpath("//title/text()")[0]
        item['url'] = response.url

        yield Item(item)
