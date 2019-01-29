#! /usr/bin/env python3

import os
import time

def nginx_logs_backup():
    # 根据实际路径修改变量内容
    nginx_path = '/usr/local/webserver/nginx' # nginx 目录绝对路径
    nginx_log_path = nginx_path + '/logs' # nginx 的日志存储路径
    nginx_logs_filename = ['access.log','host.access.log','nginx_error.log',\
                           'error.log','monitor.access.log']  # 要备份的 log 文件名
    nginx_logs_backup_path = '/usr/local/webserver/nginx/backuplogs'  # 备份文件目的路径


    nginx_pid_path = nginx_log_path +'/' +'nginx.pid'
    nginx_pid = os.popen('cat '+ nginx_pid_path).read()[:-1]   # 获取 nginx 当前 pid

    date = time.strftime("%Y%m%d", time.localtime()) # 获取当前日期

    os.system('mkdir '+nginx_logs_backup_path+'/'+date+'_backup_logs') # 生成当天日志备份目录

    os.system('kill -TERM '+ nginx_pid) # 关闭 nginx

    for n in range(len(nginx_logs_filename)):
        logs_filename_path = nginx_log_path + '/' + nginx_logs_filename[n]
        # 移动log文件并在日志名前添加当前日期
        os.system('mv '+logs_filename_path +' '+nginx_logs_backup_path+'/'+date+'_backup_logs/'+date+'_'+nginx_logs_filename[n])

    os.system(nginx_path+'/sbin/nginx') # 重启 nginx


if __name__  ==  '__main__':
    nginx_logs_backup()





