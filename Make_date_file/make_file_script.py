#! /usr/bin/env python3

import os

def make_date_format():
    mounth_list = list(range(1,13))
    day_list = list(range(1,32))

    # 修改列表内容的类型并在个位前面加0
    for n in range(12):
        mounth_list[n] = str(mounth_list[n])
        if n <= 8:
            mounth_list[n] = '0'+mounth_list[n]

    for n in range(31):
        day_list[n] = str(day_list[n])
        if n <= 8:
            day_list[n] = '0'+day_list[n]

    # 生成一年内每天的日期
    date_format = []
    for m in range(12):
        if m == 1:
            for n in range(29):
                date_format.append(mounth_list[m]+day_list[n])
        elif m == 3 or m == 5 or m == 8 or m == 10:
            for n in range(30):
                date_format.append(mounth_list[m]+day_list[n])
        else:
            for n in range(31):
                date_format.append(mounth_list[m]+day_list[n])
    return date_format

def make_files(date_format):
    # 执行命令批量生成文件或目录
    for n in range(len(date_format)):
        filename_format = '2019'+date_format[n]+'_backup_logs'
        command = 'mkdir'+' '
        os.system(command + filename_format)

if __name__ == '__main__':
    make_files(make_date_format())


    
