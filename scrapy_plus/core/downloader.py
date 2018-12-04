#coding:utf-8

import chardet
from ..http.response import Response
#import urllib2
#import socket
import requests


class Downloader(object):
    """ 框架提供的Downloader下载器原型类，由框架提供方法 请求发送和响应返回 """

    # 接收请求对象，通过requests模块发送请求，最后构建并返回自定义响应
    def send_request(self, request):


        # 如果请求方法是GET，按requests模块get发送
        if request.method.upper() == "GET":
            response = requests.get(
                url=request.url,
                headers=request.headers,
                params=request.params,
                proxies=request.proxy
            )
        # 如果请求方法是POST，按requests模块post发送
        elif request.method.upper() == "POST":
            response = requests.post(
                url=request.url,
                headers=request.headers,
                params=request.params,
                data=request.formdata,
                proxies=request.proxy
            )
        # 如果既不是get也不是post，则抛出异常给用户，同时程序中断
        else:
            raise TypeError("Not Support Request Method : {}".format(request.method))

        # 如果上面代码没有抛出异常，则正常返回自定义响应给引擎
        return Response(
            # 响应url地址
            url=response.url,
            # 响应体（网页原始编码字符串）
            body=response.content,
            # 响应报头
            headers=response.headers,
            # 响应状态码
            status_code=response.status_code,
            # 响应体字符编码
            encoding=chardet.detect(response.content)['encoding']
        )

# class MethodExcepotion(Exception):
#     def __str__
