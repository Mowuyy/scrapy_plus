#coding:utf-8

from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline

from ..http.request import Request
from ..http.item import Item


class Engine(object):

    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

    def start(self):
        # 1. 从spider处获取第一个需要发送的请求
        start_request = self.spider.start_request()
        # 2. 将请求交给调度器 去重并存储到请求队列
        self.scheduler.add_request(start_request)

        # 循环获取请求，并发送请求解析响应，直到没有请求，结束循环
        while True:
            # 3. 从调度器里获取一个去重后的请求
            request = self.scheduler.get_request()
            # 如果request 是 None，则表示所有请求发送完毕，则退出循环
            if request is None:
                break
            # 4. 将请求交给下载器发送，并返回响应对象
            response = self.downloader.send_request(request)
            # 5. 将响应交给spider解析，并返回解析结果（请求Request 或 数据Item）
            item_or_request = self.spider.parse(response)

            # 6. 判断解析结果是类型：
            # 6.1 如果是Request请求，则交给调度器处理
            if isinstance(item_or_request, Request):
                self.scheduler.add_request(item_or_request)
            # 6.2 如果是Item数据，则交给管道处理
            elif isinstance(item_or_request, Item):
                self.pipeline.process_item(item_or_request)
            # 6.3 如果既不是请求也不是item，则抛出异常给用户
            else:
                raise TypeError("Not Support Data Type : <{}> {}".format(type(item_or_request), item_or_request))




