#coding:utf-8

import json
import re
from lxml import etree

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


    def xpath(self, rule):
        """ 提供xpath解析方法"""
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)


    def re_findall(self, rule, string=None):
        """ 提供正则解析响应体，如果string有值则解析string字符串；如果string没有值则解析body响应体"""
        if string:
            return re.findall(rule, string)
        
        return re.findall(rule, self.body)

    # 当响应是一个json字符串，通过json()返回对应的python数据类型
    #requests.get().json()
    def json(self):
        return json.loads(self.body)


