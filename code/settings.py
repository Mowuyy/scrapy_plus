#coding:utf-8


######## 默认的 日志配置

 # 默认日志等级
#DEFAULT_LOG_LEVEL = logging.DEBUG
# 默认日志格式
#DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
# 默认时间格式
#DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
# 默认日志文件名称
DEFAULT_LOG_FILENAME = 'baidu.log'

# 并发类型和并发量
#ASYNC_TYPE = "thread"
ASYNC_TYPE = "coroutine"
ASYNC_COUNT = 10

# redis请求队列默认配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_QUEUE_HOST = '192.168.37.50'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 10

# redis请求指纹集合默认配置
REDIS_REDIS_NAME = 'fingerprint_fp'
REDIS_REDIS_HOST = '192.168.37.50'
REDIS_REDIS_PORT = 6379
REDIS_REDIS_DB = 10


# 非分布式
ROLE = None

# 分布式角色
#ROLE = "master"
#ROLE = "slave"


# 需要启用的爬虫
SPIDERS = [
    "spiders.baidu.BaiduSpider",
    #"spiders.douban.DoubanSpider",
]



# 需要启用的管道
PIPELINES = [
    #"pipelines.BaiduPipeline1",
    #"pipelines.BaiduPipeline2",
    #"pipelines.DoubanPipeline1",
    #"pipelines.DoubanPipeline2"
]

# 需要启用的爬虫中间件
SPIDER_MIDDLEWARES = [
    #"middlewares.BaiduSpiderMiddleware1",
    #"middlewares.BaiduSpiderMiddleware2",
    #"middlewares.DoubanSpiderMiddleware1",
    #"middlewares.DoubanSpiderMiddleware2",
]

# 需要启用的下载中间件
DOWNLOADER_MIDDLEWARES = [
    "middlewares.DownloaderMiddleware",
    #"middlewares.BaiduDownloaderMiddleware2",
    #"middlewares.DoubanDownloaderMiddleware1",
    #"middlewares.DoubanDownloaderMiddleware2",
]


