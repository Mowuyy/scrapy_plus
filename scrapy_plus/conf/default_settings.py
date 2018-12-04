#coding:utf-8


""" scrapy_plus 框架的默认配置文件，可以统一管理所有的配置参数， """


import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称



# 需要启用的爬虫
SPIDERS = [

]

# 需要启用的管道
PIPELINES = [

]

# 需要启用的爬虫中间件
SPIDER_MIDDLEWARES = [

]

# 需要启用的下载中间件
DOWNLOADER_MIDDLEWARES = [

]


# 最后导入用户运行环境下的 settings 文件里配置信息，可以覆盖框架里的同名配置参数
from settings import *

