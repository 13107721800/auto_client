

class Base(object):

    def exec_commond(self, cmd):
        if self.mode == 'agent':
            import subprocess
            res = subprocess.getoutput(cmd)
            ipinfo = res[10:20]
            print(ipinfo)
        elif self.mode == 'ssh':
            import paramiko

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

            ssh.connect(hostname='hostname', port=settings.SSH_PORT, username=settings.USER, password=settings.PWD,
                        allow_agent=False,
                        look_for_keys=False)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()
        else:
            import subprocess
            res = subprocess.getoutput("salt 'hostname' cmd.run cmd")
            print(res)