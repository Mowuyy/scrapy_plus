#coding:utf-8


class Response(object):
    """ 框架提供的Response响应类原型，由下载器Downloader构建响应对象 交给用户"""
    def __init__(self, url, body, headers, status_code, encoding):
        # 响应的url
        self.url = url
        # 响应体（网页原始编码字符串）
        self.body = body
        # 响应报头
        self.headers = headers
        # 响应状态码
        self.status_code = status_code
        # 响应体字符编码
        self.encoding = encoding


    def xpath(self):
        pass

    def re_findall(self):
        pass

    def json(self):
        pass

