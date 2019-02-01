#! /usr/bin/env python3

import os

    
# 获取待处理文件的年份和月份区间
def get_year_mounth(dir_file_list):
    year_mounth_dict = {}
    for n in range(len(dir_file_list)):
        # 获取年份作为dict的key，对应生成一个空列表装年对应的月份
        year_mounth_dict.setdefault(dir_file_list[n][:4],[])
        # 如果月份不在年份对应的value列表中则添加  
        if dir_file_list[n][4:6] not in year_mounth_dict[dir_file_list[n][:4]]:
            year_mounth_dict[dir_file_list[n][:4]].append(dir_file_list[n][4:6]) 
    return year_mounth_dict
    

# 检测classfly_path中是否已有以年为单位的分类目录，没有则创建
def year_dir_exists_test(year_mounth_dict,classfly_path,dir_name):
    for key in year_mounth_dict:
        if os.path.exists(classfly_path+'/'+ key + dir_name) == False:
            os.mkdir(classfly_path+'/'+ key + dir_name)
    return

# 检测年目录中是否已有以月为单位的分类目录，没有则创建
def mounth_dir_exists_test(year_mounth_dict,classfly_path,dir_name):
    for key,value in year_mounth_dict.items():
        for n in range(len(value)):
            mounth_dir_path = classfly_path +'/'+ key + dir_name +'/'+ key +value[n] + dir_name
            if os.path.exists(mounth_dir_path) == False:
                os.mkdir(mounth_dir_path)
    return

# 月分类移动文件
def move_files_mounth(dir_file_list,classfly_path,dir_name,dir_path):
    for n in range(len(dir_file_list)):
        year = dir_file_list[n][:4]
        mounth = dir_file_list[n][4:6]
        filename = dir_file_list[n]
        des_path = classfly_path +'/'+ year + dir_name +'/'+ year + mounth + dir_name
        os.system('mv '+ dir_path+'/'+filename+' '+des_path+'/'+filename)
    return

# 年分类移动文件
def move_files_year(dir_file_list,classfly_path,dir_name,dir_path):
    for n in range(len(dir_file_list)):
        year = dir_file_list[n][:4]
        filename = dir_file_list[n]
        des_path = classfly_path +'/'+ year + dir_name
        os.system('mv '+ dir_path+'/'+filename+' '+des_path+'/'+filename)
    return

# 分类器入口
def file_classfly(dir_path,classfly_path,dir_name):
    dir_file_list = os.listdir(dir_path)
    year_mounth_dict = get_year_mounth(dir_file_list)
    print(year_mounth_dict)

    # 按月分类
    year_dir_exists_test(year_mounth_dict,classfly_path,dir_name)
    mounth_dir_exists_test(year_mounth_dict,classfly_path,dir_name)
    move_files_mounth(dir_file_list,classfly_path,dir_name,dir_path)
    
    # 按年分类
    # year_dir_exists_test(year_mounth_dict,classfly_path,dir_name)
    # move_files_year(dir_file_list,classfly_path,dir_name,dir_path)

if __name__ == '__main__':
    
    dir_path = '/home/sunnylinux/pythontest/python3_script/mk_file_test_mounth'
    classfly_path = '/home/sunnylinux/pythontest/python3_script/backuplog_classfly_mounth'
    dir_name = '_backup_logs'
    
    file_classfly(dir_path,classfly_path,dir_name)
