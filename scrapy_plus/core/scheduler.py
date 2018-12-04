#coding:utf-8

# try:
#     from Queue import Queue
# except:
#     from queue import Queue



from ..conf.default_settings import *

if ROLE is None:
    from six.moves.queue import Queue
    from ..utils.set import PythonFilterSet as Set
elif ROLE == "master" or ROLE == "slave":
    from ..utils.queue import Queue
    from ..utils.set import RedisFilterSet as Set
else:
    raise TypeError("Not Support Role Type : {}".format(ROLE))



from ..utils.log import logger

import six
import w3lib.url
from hashlib import sha1
from six.moves.urllib.parse import urlencode

class Scheduler(object):
    """ 框架提供的Scheduler调度器原型类，由框架提供方法 处理请求去重和请求存储 """

    def __init__(self):
        # 请求队列
        self.request_queue = Queue()
        # 指纹集合
        self.fp_set = Set()

        # 请求计数器
        self.request_count = 0

    def add_request(self, request):
        if request.dofilter:
            # 每次来一个新的请求，能获取该请求的指纹字符串
            fp = self._get_fingerprint(request)
            # 判断请求是否是重复请求，如果不是则添加到请求队列中
            if self._filter_request(request, fp):
                # 将请求添加到请求队列中
                self.request_queue.put(request)
                # 每次存入一个新的请求，则让请求计数器自增1
                self.request_count += 1
                # 同时记录请求指纹
                #self.fp_set.add(request.url)
                #self.fp_set.add(fp)
                self.fp_set._add_fp(fp)
        else:
            self.request_queue.put(request)
            self.request_count += 1


    def _filter_request(self, request, fp):
        # 判断请求指纹是否在指纹集合内，如果在集合内，则表示该请求之前发送过，不允许放入请求队列
        #if request.url in self.fp_set:
        #if fp in self.fp_set:
        if self.fp_set._is_filter(fp):
            logger.warning("Filter Request [{}] <{}>".format(request.method, request.url))
            return False
        # 如果请求指纹不在集合里，则允许放入请求队列
        else:
            return True


    def _get_fingerprint(self, request):
        # 对请求url地址规整处理
        url = request.url.lower()
        url = w3lib.url.canonicalize_url(url)

        # 请求方法统一转大写
        method = request.method.upper()

        # 请求的查询数据
        params = request.params
        if params is None:
            params = ""
        elif isinstance(params, dict):
            params = urlencode(params)
        else:
            params = params

        # 请求的表单数据
        formdata = request.formdata
        if formdata is None:
            formdata = ""
        elif isinstance(formdata, dict):
            formdata = urlencode(formdata)
        else:
            formdata = formdata

        s1 = sha1()

        s1.update(self._get_utf8_string(url))
        s1.update(self._get_utf8_string(method))
        s1.update(self._get_utf8_string(params))
        s1.update(self._get_utf8_string(formdata))

        fp = s1.hexdigest()

        return fp


    def _get_utf8_string(self, string):
        """ 接收任意python版本的任意编码字符串，都能返回一个非Unicode字符串"""
        if six.PY2:
            # str非Unicode, unicode是Unicode
            if isinstance(string, str):
                return string
            else:
                return string.encode("utf-8")
        elif six.PY3:
            if isinstance(string, bytes):
                return string
            else:
                return string.encode("utf-8")
        else:
            raise Exception("Not Support Python 4")


            # bytes, str

    def get_request(self):
        # 从队列里获取一个请求
        if not self.request_queue.empty():
            return self.request_queue.get()


        # try:
        #     return self.request_queue.get(False)
        # except:
        #     return None

