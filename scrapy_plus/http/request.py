#coding:utf-8


class Request(object):
    """ 框架提供的Request请求类原型，需要用户使用该类构建 请求对象 """
    def __init__(self, url, headers=None, params=None, formdata=None, method="GET", proxy=None):
        # 请求的url地址（必须提供）
        self.url = url
        # 请求报头
        self.headers = headers
        # 查询字符串 或 字典
        self.params = params
        # 表单数据字符串 或 字典
        self.formdata = formdata
        # 请求方法（默认是GET）
        self.method = method
        # 代理服务器
        self.proxy = proxy

