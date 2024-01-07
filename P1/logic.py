# 判断CPU的监控数值是否达到预警
import datetime
import time
import random

devices = ['huawei', 'cisco', 'h3c', 'juniper']
ip_list = ['192.168.1.1',
           '10.10.1.1',
           '172.16.1.1',
           '200.207.1.1']
location = ['北京', '深圳', '成都', '西安']


def write_log(cpu, level, info):
    now_time = str(datetime.datetime.now()).split('.')[0]
    log_line = f"{now_time} %{level} 设备{info[0]}(IP为{info[1]}, 位置在{info[2]})的CPU使用率目前是{cpu}%.\n"
    with open('log/cpu.log', 'a') as f:
        f.write(log_line)


def check_cpu(hostname, ip, localtion):
    cpu_usage = random.randint(0, 100)
    info = [hostname, ip, localtion]
    if cpu_usage < 60:
        write_log(cpu_usage, 'Info', info)
    elif 60 <= cpu_usage < 85:
        write_log(cpu_usage, 'Alert', info)
    else:
        write_log(cpu_usage, 'Error', info)
    print(f'{hostname}: {cpu_usage}')
    time.sleep(random.randint(1, 5))


while True:
    for i in range(len(devices)):
        check_cpu(devices[i], ip_list[i], location[i])








