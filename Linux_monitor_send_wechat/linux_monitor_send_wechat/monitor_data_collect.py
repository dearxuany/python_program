import psutil
import socket
from datetime import datetime
import time

# 字节单位转换
def change_measure_unit(n):
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}  
    # 给单位赋值如K的值为1024字节存在prefix字典中
    for i,s in enumerate(symbols):
        prefix[s]= 1 << (i+1)*10  # 二进制右移
    # reverse是为了减少循环次数，不需要由小到大一个个判断
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n)/prefix[s]
            return '{:.2f}{}B'.format(value,s)


def get_cpu_info():
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)  # 间隔为1s
    return dict(cpu_count=cpu_count,cpu_percent=cpu_percent)

def get_memory_info():
    mem_total = change_measure_unit(psutil.virtual_memory().total)
    mem_percent = psutil.virtual_memory().percent
    mem_used = change_measure_unit(psutil.virtual_memory().total*mem_percent/100)
    mem_available = change_measure_unit(psutil.virtual_memory().available)
    return dict(mem_total=mem_total,mem_percent=mem_percent,
                mem_used=mem_used,mem_available=mem_available) 

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total = change_measure_unit(disk_usage.total)
    disk_percent = disk_usage.percent
    disk_used = change_measure_unit(disk_usage.used)
    disk_available = change_measure_unit(disk_usage.free)
    return dict(disk_total=disk_total,disk_percent=disk_percent,
                disk_used=disk_used,disk_available=disk_available)

def get_boottime_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
    return dict(boot_time=boot_time) 

def get_collect_time():
    collect_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    return dict(collect_time=collect_time)

def get_host_name():
    host_name = socket.gethostname()
    return dict(host_name=host_name)


# 将以上所有信息存放在一个空字典中
def collect_monitor_data():
    monitor_data = {}
    monitor_data.update(get_collect_time())
    monitor_data.update(get_host_name())
    monitor_data.update(get_boottime_info())
    monitor_data.update(get_cpu_info())
    monitor_data.update(get_memory_info())
    monitor_data.update(get_disk_info())
    return monitor_data

