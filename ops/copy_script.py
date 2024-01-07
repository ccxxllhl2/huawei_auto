import paramiko

local_file = "ops_demo.py"
remote_file = "auto_del_startup.py"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="192.168.1.55",
            port=22,
            username="huaweiuser",
            password="Huawei@123")

sftp = ssh.open_sftp()
sftp.put(local_file, remote_file)

ssh.close()