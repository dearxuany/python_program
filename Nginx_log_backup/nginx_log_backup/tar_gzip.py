#! /usr/bin/env python3

import os

# 打包当前目录中的内容
def tar_first_dir(dir_list):
    for n in range(len(dir_list)):
        tar_filename = tar_path+'/'+ dir_list[n]
        os.system('tar -czf {}.tar.gz -C{} {}'.format(tar_filename,start_path,dir_list[n]))

# 打包当前目录中的目录的下一层目录
def tar_second_dir(dir_list):
    second_dirlist_dict = {}
    for n in range(len(dir_list)):
        second_dirlist_dict.setdefault(dir_list[n],[])
        second_dir_path = start_path+'/'+ dir_list[n]
        second_dir_list = os.listdir(second_dir_path)
        second_dirlist_dict[dir_list[n]].extend(second_dir_list)
    

    for key,value in second_dirlist_dict.items():
        if os.path.exists(tar_path+'/'+key) == False :
            os.system('mkdir '+tar_path+'/'+key)
        for n in range(len(value)):
            tar_filename = tar_path + '/' + key + '/'+ value[n]
            os.system('tar -czf {}.tar.gz -C{} {}'.format(tar_filename,start_path+'/'+key,value[n]))



def tar_gzip(startpath,tarpath):
    global start_path
    global tar_path

    start_path = startpath
    tar_path = tarpath

    dir_list = os.listdir(start_path)

    # 打包压缩指定目录中的内容
    # tar_first_dir(dir_list)
    
    # 分别打包压缩指定目录中所有子目录中的内容
    tar_second_dir(dir_list)
    

if __name__ == '__main__':
    start_path = '/home/sunnylinux/pythontest/python3_script/backuplog_classfly_mounth'  # 要打包压缩目录所在的目录路径
    tar_path = '/home/sunnylinux/pythontest/python3_script/tar_logs_mounth'  # 打包压缩文件要存放的目录路径
    
    tar_gzip(start_path,tar_path)
