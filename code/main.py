#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy_plus.core.engine import Engine

# from spiders.baidu import BaiduSpider
# from spiders.douban import DoubanSpider


# from pipelines import BaiduPipeline1, BaiduPipeline2, DoubanPipeline1, DoubanPipeline2

# from middlewares import BaiduSpiderMiddleware1, BaiduSpiderMiddleware2, BaiduDownloaderMiddleware1, BaiduDownloaderMiddleware2, DoubanSpiderMiddleware1, DoubanSpiderMiddleware2, DoubanDownloaderMiddleware1, DoubanDownloaderMiddleware2

# from settings import SPIDERS

# import importlib

import time


def main():

    engine = Engine()

    while True:
        engine.start()
        time.sleep(5)

    # path = SPIDERS[0]

    # index = path.rfind(".")

    # print(path[:index])
    # print(path[index+1:])

    # module_path = importlib.import_module("spiders.baidu")
    # cls = getattr(module_path, "BaiduSpider")
    # print(cls)
    # print(BaiduSpider)

    # getattr(对象, "属性/方法")
    # getattr(模块路径, "类")


    # # 通过字典保存多个需要执行的爬虫， 爬虫名：爬虫对象
    # spiders = {BaiduSpider.name : BaiduSpider(), DoubanSpider.name : DoubanSpider()}

    # # 表示多个管道的列表
    # pipelines = [
    #     BaiduPipeline1(),
    #     BaiduPipeline2(),
    #     DoubanPipeline1(),
    #     DoubanPipeline2()
    # ]

    # # 所有 爬虫中间件
    # spider_middlewares = [
    #     BaiduSpiderMiddleware1(),
    #     BaiduSpiderMiddleware2(),
    #     DoubanSpiderMiddleware1(),
    #     DoubanSpiderMiddleware2()
    # ]

    # # 所有的下载中间件
    # downloader_middlewares = [
    #     BaiduDownloaderMiddleware1(),
    #     BaiduDownloaderMiddleware2(),
    #     DoubanDownloaderMiddleware1(),
    #     DoubanDownloaderMiddleware2()
    # ]


    # engine = Engine(spiders, pipelines, spider_middlewares, downloader_middlewares)



if __name__ == '__main__':
    main()
