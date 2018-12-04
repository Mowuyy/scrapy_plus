#coding:utf-8

from ..http.request import Request
from ..http.item import Item

class Spider(object):
    """ 框架提供的Spider爬虫原型类，用户可以通过继承 重写类属性和类方法 """

    # 第一个需要发送的url地址（可以被子类重写）
    start_url = "http://www.baidu.com/"


    def start_request(self):
        # 返回第一个请求给引擎
        return Request(self.start_url)


    def parse(self, response):
        # 接收响应，提取数据，并返回item 或 request 给引擎
        data = {"status" : response.status_code, "url" : response.url, "content" : response.body}

        return Item(data)



