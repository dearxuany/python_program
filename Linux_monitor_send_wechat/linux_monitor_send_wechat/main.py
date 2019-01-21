#! /usr/bin/env python3

import monitor_data_collect
import send_wechat

def main():
    data =  monitor_data_collect.collect_monitor_data()
    content = 'linux 系统性能监控\n'\
              +'采集时间：{}\n'.format(data['collect_time'])\
              +'主机名：{}\n'.format(data['host_name'])\
              +'开机时间：{}\n'.format(data['boot_time'])\
              +'CPU个数：{}\n'.format(data['cpu_count'])\
              +'CPU使用率：{}\n'.format(data['cpu_percent'])\
              +'内存总量：{}\n'.format(data['mem_total'])\
              +'内存利用率：{}\n'.format(data['mem_percent'])\
              +'内存已用空间：{}\n'.format(data['mem_used'])\
              +'内存可用空间：{}\n'.format(data['mem_available'])\
              +'磁盘总量：{}\n'.format(data['disk_total'])\
              +'磁盘利用率：{}\n'.format(data['disk_percent'])\
              +'磁盘已用空间：{}\n'.format(data['disk_used'])\
              +'磁盘可用空间：{}\n'.format(data['disk_available'])

    send_wechat.send_massage(content)

if __name__ == '__main__':
    main()
