# coding=utf-8
class ResultBean(dict):
    def __init__(self):
        dict.__init__(self)  # 继承pyton字典类的方法和属性

    def seet(self):
        self['abc'] = 'asss'

        return self
