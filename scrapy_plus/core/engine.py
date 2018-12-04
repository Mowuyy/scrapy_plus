#coding:utf-8

# 获取模块的绝对路径
import importlib
from datetime import datetime

from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline

from ..http.request import Request
from ..http.item import Item

# 导入日志系统的日志对象
from ..utils.log import logger

from ..conf.default_settings import *


class Engine(object):

    #def __init__(self, spiders, pipelines, spider_middlewares, downloader_middlewares):
    def __init__(self):
        #self.spider = Spider()
        #self.spiders = spiders
        self.spiders = self._auto_import_module(SPIDERS, True)

        self.scheduler = Scheduler()
        self.downloader = Downloader()
        #self.pipeline = Pipeline()
        #self.pipelines = pipelines
        self.pipelines = self._auto_import_module(PIPELINES)
        # 爬虫中间件
        #self.spider_mids = spider_middlewares
        self.spider_mids = self._auto_import_module(SPIDER_MIDDLEWARES)
        # 下载中间件
        #self.downloader_mids = downloader_middlewares
        self.downloader_mids = self._auto_import_module(DOWNLOADER_MIDDLEWARES)



    def _auto_import_module(self, path_list, spider=False):

        if spider:
            instance = {}

        else:
            instance = []

        # 迭代每个配置组件的列表，迭代列表取出每个组件字符串
        for path in path_list:
            # 根据右边第一个 . 进行分隔
            index = path.rfind(".")
            # 左边是 模块的相对路径
            module_name = path[:index]
            # 右边是 类名
            class_name = path[index+1:]

            # 提供模块的相对路径，返回该模块的绝对路径
            module_path = importlib.import_module(module_name)
            # 根据模块的绝对路径，获取该模块里指定的类
            cls = getattr(module_path, class_name)

            # 构建类实例化对象，返回 字典（爬虫） 或 列表（管道、中间件）
            if spider:
                instance[cls.name] = cls()
            else:
                instance.append(cls())

        return instance




    def start(self):
        # 框架运行的开始时间
        start = datetime.now()
        logger.info("Start time : {}".format(start))

        self._start_engine()
        # 框架运行的结束时间
        end = datetime.now()
        logger.info("End time : {}".format(end))

        # 框架运行的时间
        logger.info("Using time : {} sec".format((end - start).total_seconds()))


    def _start_engine(self):
        #[(spider_name, spider), (spider_name, spider)]
        for spider_name, spider in self.spiders.items():
            # 1. 从spider处获取第一个需要发送的请求
            #start_request = self.spider.start_requests()
            for start_request in spider.start_requests():

                # 对每个请求对象做预处理，并返回处理后的请求
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request, spider)

                # 每个请求都有一个标记，爬虫名，之后可以通过爬虫名找到该请求所属的爬虫对象
                start_request.name = spider_name
                # 2. 将请求交给调度器 去重并存储到请求队列
                self.scheduler.add_request(start_request)


        # 循环获取请求，并发送请求解析响应，直到没有请求，结束循环
        while True:
            # 3. 从调度器里获取一个去重后的请求
            request = self.scheduler.get_request()
            # 如果request 是 None，则表示所有请求发送完毕，则退出循环
            if request is None:
                break

            # 根据请求所属的爬虫名，获取对应的爬虫对象
            spider = self.spiders[request.name]

            for downloader_mid in self.downloader_mids:
                request = downloader_mid.process_request(request, spider)

            # 4. 将请求交给下载器发送，并返回响应对象
            response = self.downloader.send_request(request)

            for downloader_mid in self.downloader_mids:
                response = downloader_mid.process_response(response, spider)


            # 5. 将响应交给spider解析，并返回解析结果（请求Request 或 数据Item）
            #item_or_request = self.spider.parse(response)
            #for item_or_request in self.spider.parse(response):
            parse_func = getattr(spider, request.callback)
            #parse_func = request.callback


            for item_or_request in parse_func(response):
                # 6. 判断解析结果是类型：
                # 6.1 如果是Request请求，则交给调度器处理
                if isinstance(item_or_request, Request):

                    # 对每个请求对象做预处理，并返回处理后的请求
                    for spider_mid in self.spider_mids:
                        item_or_request = spider_mid.process_request(item_or_request, spider)

                    # 给后续新的请求，传递爬虫名
                    item_or_request.name = request.name
                    self.scheduler.add_request(item_or_request)
                # 6.2 如果是Item数据，则交给管道处理
                elif isinstance(item_or_request, Item):

                    # 对每个item对象做预处理，并返回处理后的item
                    for spider_mid in self.spider_mids:
                        item_or_request = spider_mid.process_item(item_or_request, spider)

                    # 将item数据交给管道处理
                    for pipeline in self.pipelines:
                        item_or_request = pipeline.process_item(item_or_request, spider)

                    #self.pipeline.process_item(item_or_request)
                # 6.3 如果既不是请求也不是item，则抛出异常给用户
                else:
                    raise TypeError("Not Support Data Type : <{}> {}".format(type(item_or_request), item_or_request))




