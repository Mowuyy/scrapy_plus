#coding:utf-8

import time
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

if ASYNC_TYPE == "thread":
    # 导入线程池
    from multiprocessing.dummy import Pool
elif ASYNC_TYPE == "coroutine":
    from gevent.pool import Pool
    from gevent.monkey import patch_all
    patch_all()
else:
    raise TypeError("Not Support Async Type: {}".format(ASYNC_TYPE))



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

        # 创建线程池/协程池对象
        self.pool = Pool(ASYNC_COUNT)


        self.response_count = 0
        self.is_running = True

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

        logger.info("ASYNC_TYPE : [{}]".format(ASYNC_TYPE))

        if ROLE == "master" or ROLE is None:
            self._execute_start_request()
            #self.pool.apply_async(self._execute_start_request)

        if ROLE == "slave" or ROLE is None:
            # 创建了12个子线程，异步执行了12次 self._execute_request_response_item，执行完毕后，程序结束
            for _ in range(ASYNC_COUNT):
                self.pool.apply_async(self._execute_request_response_item, callback=self._callback)

#CPU -> 寄存器 -> 缓存 L1/L2/L3 -> 内存 -> 网卡 -> 固态硬盘 -> 机械硬盘 （5400 7200）

        while True:
            # 避免CPU疯狂空转，造成资源大量浪费
            time.sleep(0.1)
            # 当请求计数器和响应计数器相同时候，表示所有请求处理完毕，且不会有新的请求需要处理，则程序退出。
            # self.scheduler.request_count != 0 防止程序刚执行时直接判断都等于0相同，导致程序退出。
            if self.response_count == self.scheduler.request_count and self.scheduler.request_count != 0:
                self.is_running = False
                break

        try:
            # 关闭线程池， 不再接收新的线程任务（但是协程池没有close）
            self.pool.close()
        except:
            pass
        print("main thread")
        # 让主线程阻塞
        self.pool.join()

        logger.info("Main Thread is over!")

# apply_async(self, func, args, kwargs, errback, callback)
# apply_async(self, func, args=None, kwds=None, callback=None)

# 当所有请求发送完毕后，且没有新的请求时，则程序退出。
# 队列为空，

# 请求数 == 响应数



# 单机爬虫：


# 每次存入一个新请求，请求计数器 自增1
# 每次解析完一个响应，响应计数器 自增1

# 定律：请求一定是先存入，之后在发送请求返回响应。
# 结论：请求计数器 一定是大于 响应计数器

# 结论2：当请求计数器 等于 响应计数器时，则表示所有请求全部发送完毕，且没有新的请求存入队列，则程序可以退出。


# 分布式：
# 主：只负责存储请求，只自增请求计数器，不会自增响应计数器
# 从：只负责发送请求，只自增响应计数器，不会自增请求计数器

# 所以：请求计数器 和 响应计数器 永远不会相等。

# scrapy_redis

    def _callback(self, _):
        if self.is_running:
            time.sleep(0.01)
            self.pool.apply_async(self._execute_request_response_item, callback=self._callback)



    def _execute_start_request(self):
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


    def _execute_request_response_item(self):
        # 循环获取请求，并发送请求解析响应，直到没有请求，结束循环
        #while True:
        # 3. 从调度器里获取一个去重后的请求
        request = self.scheduler.get_request()
        # 如果request 是 None，则表示所有请求发送完毕，则退出循环
        if request is None:
            return


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

        #if self.scheduler.request_queue.empty():
        # 每次完整的解析完毕一个response响应，则响应计数器自增1（如果向盈利有新的请求被提取，则一定是先自增请求计数器）
        self.response_count += 1


