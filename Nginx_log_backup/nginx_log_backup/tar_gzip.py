#! /usr/bin/env python3

import os

# 打包当前目录中的内容
def tar_first_dir(dir_list):
    for n in range(len(dir_list)):
        goal_dir_path = start_path +'/'+ dir_list[n]
        os.system('tar -czf '+goal_dir_path+'.tar.gz '+goal_dir_path)

# 打包当前目录中的目录的下一层目录
def tar_second_dir(dir_list):
    second_dirlist_dict = {}
    for n in range(len(dir_list)):
        second_dirlist_dict.setdefault(dir_list[n],[])
        second_dir_path = start_path+'/'+ dir_list[n]
        second_dir_list = os.listdir(second_dir_path)
        second_dirlist_dict[dir_list[n]].extend(second_dir_list)

    for key,value in second_dirlist_dict.items():
        for n in range(len(value)):
            goal_dir_path = start_path + '/' + key + '/'+ value[n]
            os.system('tar -czf '+goal_dir_path+'.tar.gz '+goal_dir_path) 


def tar_gzip(startpath):
    start_path = startpath
    dir_list = os.listdir(start_path)

    # 打包当前目录中的内容
    tar_first_dir(dir_list)
    
    # 打包当前目录的下一级目录中的内容
    # tar_second_dir(dir_list)
    

if __name__ == '__main__':
    start_path = '/usr/local/webserver/nginx/classfly_backuplogs'
    
    tar_gzip(start_path)
