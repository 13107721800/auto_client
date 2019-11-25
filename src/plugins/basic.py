# 采集服务器基本信息
from lib.config.settings import settings
from .base import Base


class Basic(object):

    def process(self, command_func):
        res = command_func('uname')
        self.parse(res)

    def parse(self, res):
        pass
