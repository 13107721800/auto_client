import requests
import json
from lib.config.settings import settings
from src.plugins import PluginsManager
import os


class Base(object):
    def postData(self, res):
        requests.post(settings.API_URL, data=json.dumps(res))


# 采集信息，发送
class Agent(Base):

    # 采集信息
    def collect(self):
        res = PluginsManager().execute()
        hostname = res['basic']['data']['hostname']
        # self.postData(res)
        # print(res)
        ret = open(os.path.join(settings.BASEDIR, 'conf/cert'), 'r', encoding='utf-8').read()
        if not ret:
            with open(os.path.join(settings.BASEDIR, 'conf/cert'), 'w', encoding='utf-8') as f:
                f.write(hostname)
        else:
            res['basic']['data']['hostname'] = ret
        for key, val in res.items():
            print(key, val)

        self.postData(res)


class SSHSalt(Base):

    def get_hostname(self):
        res = requests.post(settings.API_URL)
        hostname_list = res.text
        return hostname_list

    def task(self, hostname):
        res = PluginsManager(hostname).execute()
        self.postData(res)

    def collect(self):
        from concurrent.futures import ThreadPoolExecutor
        hostname_list = self.get_hostname()
        p = ThreadPoolExecutor(10)
        for hostname in hostname_list:
            p.submit(self, hostname)
