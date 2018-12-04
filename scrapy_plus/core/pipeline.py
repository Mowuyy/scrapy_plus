#coding:utf-8


class Pipeline(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """

    def process_item(self, item):
        # 接收 item 数据，做后续处理
        print("[Pipeline] process_item : [{}] <{}> {}".format(item.data['status'], item.data['url'], item.data['content']))

