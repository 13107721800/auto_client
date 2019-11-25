# 用户自定义配置
import os


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)

USER = 'root'
PWD = 1

SSH_USER = 'root'
SSH_PWD = 1
SSH_PORT = 22

MODE = 'agent'

PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
    # 'cpu': 'src.plugins.cpu.Cpu',
    # 'disk': 'src.plugins.disk.Disk',
    # 'memory': 'src.plugins.memory.Memory',
}

API_URL = 'http://127.0.0.1:8000/asset/'
