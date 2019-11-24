import os
from . import global_settings
from conf import setting
import importlib


class Settings():
    def __init__(self):
        # 获取自定义的配置的路径
        # conf_str = os.environ.get('USER_SETTING')
        # 获取默认的配置
        for name in dir(global_settings):
            if name.isupper():
                # 获取默认配置中对应属性的值
                val = getattr(global_settings, name)
                # 给settings对象设置属性
                setattr(self, name, val)
        # 获取自定义的配置
        # module = importlib.import_module(conf_str)
        for name in dir(setting):
            if name.isupper():
                # 获取默认配置中对应属性的值
                val = getattr(setting, name)
                # 给settings对象设置属性
                setattr(self, name, val)


settings = Settings()
