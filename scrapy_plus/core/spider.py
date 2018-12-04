#coding:utf-8

from ..http.request import Request
from ..http.item import Item

class Spider(object):
    """ 框架提供的Spider爬虫原型类，用户可以通过继承 重写类属性和类方法 """

    # 第一个需要发送的url地址（可以被子类重写）
    #start_url = "http://www.baidu.com/"

    start_urls = []


    def start_requests(self):
        for url in self.start_urls:
            # 返回第一个请求给引擎
            yield Request(url, callback="parse")


        # request_list = []
        # for url in self.start_urls:
        #     request_list.append(Request(url))
        # return request_list


    def parse(self, response):
        raise Exception("Must overwrite parse func")



