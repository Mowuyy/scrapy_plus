#coding:utf-8

# try:
#     from Queue import Queue
# except:
#     from queue import Queue

from six.moves.queue import Queue


class Scheduler(object):
    """ 框架提供的Scheduler调度器原型类，由框架提供方法 处理请求去重和请求存储 """

    def __init__(self):
        # 请求队列
        self.request_queue = Queue()
        # 指纹集合
        self.fp_set = set()

    def add_request(self, request):
        # 判断请求是否是重复请求，如果不是则添加到请求队列中
        if self._filter_request(request):
            # 将请求添加到请求队列中
            self.request_queue.put(request)
            # 同时记录请求指纹
            self.fp_set.add(request.url)


    def _filter_request(self, request):
        # 判断请求指纹是否在指纹集合内，如果在集合内，则表示该请求之前发送过，不允许放入请求队列
        if request.url in self.fp_set:
            return False
        # 如果请求指纹不在集合里，则允许放入请求队列
        else:
            return True


    def get_request(self):
        # 从队列里获取一个请求
        if not self.request_queue.empty():
            return self.request_queue.get()


        # try:
        #     return self.request_queue.get(False)
        # except:
        #     return None

