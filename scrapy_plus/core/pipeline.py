#coding:utf-8




class Pipeline(object):
    """ 框架提供的管道原型类，用户可以通过继承 重写类方法 """

    def process_item(self, item, spider):
        return item



