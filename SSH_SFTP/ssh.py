import paramiko #完成SSH功能
import time #提供时间等待功能


class Yeslab:
    def __init__(self):
        self.ssh_inst = self.ssh_conn()
        self.shell = self.ssh_inst.invoke_shell()
        self.send_cmd('screen-length 0 temporary\n')

    def ssh_conn(self):
        ssh_inst = paramiko.SSHClient()
        ssh_inst.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        ssh_inst.connect(hostname='192.168.56.100',
                         username='yeslab',
                         password='Huawei@123')
        return ssh_inst

    def ssh_close(self, ssh_inst):
        ssh_inst.close()

    def send_cmd(self, cmd):
        self.shell.send(cmd)
        time.sleep(1)
        return self.shell.recv(9999).decode()


def operation():
    yeslab = Yeslab()
    # 任务1：SSH获取Versio, Interface, CPU
    with open('cmd.txt') as f:
        cmd_list = f.readlines()
    for cmd in cmd_list:
        result = yeslab.send_cmd(cmd)
        print(result)

    # 任务2：开启SFTP，将交换机配置备份到本地
    yeslab.send_cmd('save\ny\n')
    yeslab.ssh_close(yeslab.ssh_inst)

    new_ssh = yeslab.ssh_conn()
    sftp_inst = new_ssh.open_sftp()
    sftp_inst.get('/vrpcfg.cfg', 'config_back.cfg')
    yeslab.ssh_close(new_ssh)

if __name__ == "__main__":
    operation()