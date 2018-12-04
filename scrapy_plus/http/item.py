#coding:utf-8


class Item(object):
    """ 框架提供的Item类原型，用户需要通过这个类 构建 item对象来保存解析结果 """
    def __init__(self, data):
        # 解析结果（建议用字典）
        self._data = data

    # 只允许用户访问，不允许用户修改，保护数据
    @property
    def data(self):
        return self._data

