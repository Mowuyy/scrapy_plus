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

# 需要启用的爬虫
SPIDERS = [
    "spiders.baidu.BaiduSpider",
    "spiders.douban.DoubanSpider",
]


# 需要启用的管道
PIPELINES = [
    #"pipelines.BaiduPipeline1",
    "pipelines.BaiduPipeline2",
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
#DOWNLOADER_MIDDLEWARES = [
    #"middlewares.BaiduDownloaderMiddleware1",
    #"middlewares.BaiduDownloaderMiddleware2",
    #"middlewares.DoubanDownloaderMiddleware1",
    #"middlewares.DoubanDownloaderMiddleware2",
#]


