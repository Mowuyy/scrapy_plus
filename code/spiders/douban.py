#coding:utf-8


from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.http.item import Item

class DoubanSpider(Spider):

    name = "douban"

    start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]


    def parse(self, response):
        link_list = response.xpath("//div[@class='hd']/a/@href")

        for link in link_list:
            #yield Request(link, callback="parse_detail")
            yield Item({"detail_link" : link})


    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath("//title/text()")[0]
        item['url'] = response.url

        yield Item(item)


