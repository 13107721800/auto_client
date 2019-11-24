from lib.config.settings import settings
import importlib


class PluginsManager(object):

    def __init__(self, hostname=None):
        self.plugins_dict = settings.PLUGINS_DICT
        self.mode = settings.MODE
        self.hostname = hostname

        if self.mode == 'ssh':

            self.user = settings.SSH_USER
            self.pwd = settings.SSH_PWD
            self.port = settings.SSH_PORT

    def execute(self):
        # 获取配置文件PLUGINS_DICT值
        response = {}
        for k, v in self.plugins_dict.items():
            module_name, class_name = v.rsplit('.', 1)
            module_path = importlib.import_module(module_name)
            cls = getattr(module_path, class_name)
            res = cls().process(self.cmd_run)
            response[k] = res

        return response

    def cmd_run(self, cmd):
        if self.mode == 'agent':
            return self.cmd_agent(cmd)
        elif self.mode == 'ssh':
            return self.cmd_ssh(cmd)
        elif self.mode == 'salt':
            return self.cmd_salt(cmd)
        else:
            raise Exception('只支持三种模式：agent/ssh/salt')
        # if self.mode == 'agent':
        #     import subprocess
        #     res = subprocess.getoutput(cmd)
        #     ipinfo = res[10:20]
        #     print(ipinfo)
        # elif self.mode == 'ssh':
        #     import paramiko
        #     ssh = paramiko.SSHClient()
        #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #     # pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        #
        #     ssh.connect(hostname='hostname', port=settings.SSH_PORT, username=settings.USER, password=settings.PWD,
        #                 allow_agent=False,
        #                 look_for_keys=False)
        #     stdin, stdout, stderr = ssh.exec_command(cmd)
        #     result = stdout.read()
        #     ssh.close()
        #     return result
        # else:
        #     import  subprocess
        #     res = subprocess.getoutput("salt 'hostname' cmd.run cmd")
        #     return res

    def cmd_agent(self, cmd):
        import subprocess
        res = subprocess.getoutput(cmd)
        ipinfo = res[10:20]
        #print(ipinfo)

    def cmd_ssh(self, cmd):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

        ssh.connect(hostname=self.hostname, port=self.port, username=self.user, password=self.pwd,
                    allow_agent=False,
                    look_for_keys=False)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result

    def cmd_salt(self, cmd):
        import subprocess
        res = subprocess.getoutput("salt '%s' cmd.run '%s'" % (self.hostname, cmd))
        return res
