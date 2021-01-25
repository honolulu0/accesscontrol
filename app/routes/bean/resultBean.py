# coding=utf-8
class ResultBean(dict):

    def __init__(self):
        # dict.__init__(self)  # 继承pyton字典类的方法和属性
        super(ResultBean, self).__init__()

    def data(self, data):
        self.dict_set("data", data)
        return self

    def success(self):
        self.code(1)
        return self

    def success_msg(self, message):
        self.code(1)
        self.dict_set("message", message)
        return self

    def fail(self):
        self.code(0)
        return self

    def fail_msg(self, message):
        self.code(1)
        self.dict_set("message", message)
        return self

    def message(self, message):
        self.dict_set("message", message)
        return self

    def code(self, code):
        self.dict_set("code", code)
        return self

    def dict_set(self, key, value):
        # self.update(key= value)
        self[key] = value
