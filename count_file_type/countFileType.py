#! /usr/bin/env python3
#_*_ coding:utf-8 _*_


import os.path


rootFolder = '/sdata/www'


#后缀名字典表
result = {'folder':0}


def statistic(folder):
    for temp in os.listdir(folder):
        filepath = os.path.join(folder,temp)
        
        #判断是否文件夹，如果是文件夹，则继续递归遍历
        if (os.path.isdir( filepath )):
            result['folder'] += 1
            statistic(filepath)
        else:
            (name, extension)= os.path.splitext(temp)
            #判断后缀名是否在后缀名字典表中
            #如果有，直接将该后缀名文件数加1
            if result.has_key(extension):
                result[extension] += 1
            #如果没有，则添加新的字典项目，该后缀名文件数置位1
            else:
                result[extension] = 1
                
if __name__ == '__main__':
    statistic( rootFolder )
    sum = 0
    for name in result.keys():
        if( name == '' ):
            print('该文件夹下共有类型为【无后缀名】的文件%s个'%(result[name]))
        else:
            print('该文件夹下共有类型为【%s】的文件%s个'%(name, result[name]))
        sum += result[name]
    print("共有目录及文件%s个"%sum)


