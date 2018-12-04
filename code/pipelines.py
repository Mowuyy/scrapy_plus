#coding:utf-8



class BaiduPipeline1(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """
    def process_item(self, item, spider):
        if spider.name == "baidu":
            # 接收 item 数据，做后续处理
            print(u"[BaiduPipeline1] process_item : [{}] <{}> ".format(item.data['title'], item.data['url']))
        return item


class BaiduPipeline2(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """
    def process_item(self, item, spider):
        if spider.name == "baidu":
        # 接收 item 数据，做后续处理
            print(u"[BaiduPipeline2] process_item : [{}] <{}> ".format(item.data['title'], item.data['url']))
        return item


class DoubanPipeline1(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """
    def process_item(self, item, spider):
        if spider.name == "douban":
         # 接收 item 数据，做后续处理
            print(u"[DoubanPipeline1] process_item : [{}] <{}> ".format(item.data['title'], item.data['url']))
        return item


class DoubanPipeline2(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """
    def process_item(self, item, spider):
        if spider.name == "douban":
            # 接收 item 数据，做后续处理
            print(u"[DoubanPipeline2] process_item : [{}] <{}> ".format(item.data['title'], item.data['url']))
        return item


