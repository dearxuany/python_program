# Python3 实现 NginX 日志定时切分备份
## 项目介绍
NginX 是现行阶段常用的 Web 服务器软件，根据其配置文件，可以选择将网站的访问记录和错误记录分别记录在 access.log 和 error.log 中。
不但可以给网站整体设置 log，还可细分到各个页面，给网站内的每一个页面设置一个专属的细分 log，以便日后的访问数据统计、分析、总结，为业务和网站系统的进一步改进提供数据支撑。
随着时间的推移和服务的发展，单位时间内访问网站的人数可能会逐渐增多，被细分出来的 log 数量也越来越多，容易造成单个 log 文件记录数据量大以及 log 文件数量多而杂的问题。
这些多而大的 log 文件们会占据系统大量的存储资源、降低系统的性能。与此同时，如果系统出现问题导致 log 文件丢失，公司就会损失大量的网站数据。</br>
</br>
为解决这一问题，可以根据网站的实际运行状况，制定一个合适的频率来对 Nginx 的 log 进行定时切分，让不同时间段的访问和错误数据分别记录到不同的 log 中，防止出现单个 log 文件过大、记录数据过多的问题。
与此同时，还需要将旧的 log 文件从 NginX 指定的 logs 目录定时移动到其他地方，防止 log 文件数量过多、占用系统存储空间过多、NginX性能下降以及 log 文件丢失的问题发生。</br>
</br>
本项目主要使用 Python3 自带的 os 模块和 time 模块，配合 linux 的 crontab 定时任务以及借助 Nginx 本身的一些特性，来实现对 Nginx logs 文件的定时自动切分和备份功能。除此之外，本项目还利用了 Pyhton3 的 os 模块来实现了对备份目录的日期分类和压缩功能，为后续的备份目录处理提供方便。</br>
本项目主要有以下几个特点：</br>
* 脚本程序每执行一次都会对指定的 Nginx log 文件进行一次切分，程序会将当前在 Nginx logs 目录中的 log 文件按备份日期时间改名并移动到指定的备份目录中；</br>
* 日常可配合 linux 的 crontab 定时任务来使用，在每天的指定时间执行程序，自动对当前的日志进行切分和备份，提高任务完成效率，减少人工干预造成的错误；</br>
* 在特殊的情况下，可直接手动执行同一脚本对 Nginx 日志进行及时的切分备份，备份逻辑上不会与自动备份有冲突，不需要对备份目录和日志文件做额外的改名、迁移处理；</br>
* 项目提供一个可按年或月份来对 nginx 备份目录进行分类的脚本，可自动且快速地将以"YYmmdd"日期信息作名称开头的目录或文件进行按年份或月份进行分类，分类脚本适用于多种场景，方便高效；</br>
* 项目中还包含一个批量压缩的脚本，能批量对目录或文件进行压缩处理，除了能压缩当前目录中的所有目录外，还可选压缩当前目录的子目录中的内容，免去逐个手动遍历各个目录再进行压缩的繁琐过程，大大降低时间成本。</br>

## 项目结构说明
```
Nginx_log_backup
├── bin
├── include
├── nginx_log_backup
│   ├── files_classifier.py
│   ├── nginx_log_backup.py
│   └── tar_gzip.py
├── README.md
└── requirements.txt
```
目录 ./nginx_log_backup 存放本项目的主要代码，本项目最主要的部分是实现nginx日志分割备份功能的 nginx_log_backup.py ，files_classifier.py 是一个日期分类脚本，tar_gzip.py 是一个批量打包脚本。
requirements.txt 标有本项目的外部 Python 包列表，README.md 为项目使用说明。</br>
### nginx_log_backup.py 
nginx_log_backup.py 是本项目的 nginx 日志备份模块，是本项目最主要的功能模块，使用 Python3 的 os、time 模块配合 linux 的 crontab 定时任务实现 nginx 的日志自动定时分割备份功能，也可直接作为脚本手动执行以应对特殊状况下的应急分割备份。</br>

程序会自动检测备份目录中是否已存在当天对应的备份目录：</br>
* 如果该备份目录中没有当天的日志备份目录，则自动生成一个包含当天日期信息的目录，命名格式为“YYmmdd_backup_logs”；</br>
* 如果当天的备份目录已存在则不生成，继续使用该目录对当天 log 进行备份。</br>

对应备份 log 文件的处理：</br>
* 将要被备份的 log 文件会被改名为“YYmmdd_HHMMSS_原本名称”标有备份日期、备份时间的形式，然后被移动到上述所说当天的备份目录中；</br>
* 程序每执行一次就是一次对 nginx 日志的分片，日志文件被移走备份后，nginx 在重启的过程中会自动生成新的日志文件在其指定使用的 logs 目录中；</br>
* 此时间点以后的连接、错误数据会被记录在这些新log中，直到下一次分片备份。</br>
### files_classifier.py
files_classifier.py 是一个日期分类模块，为 nginx 日志备份目录提供后续的分类处理，本模块主要使用的是 Python3 的 os 模块。分类模块可选两种分类模式：按年份分类、按月份分类，可按需选择。可配合 crontab 定时任务使用，定期对 nginx 日志备份目录进行自动分类。本模块可单独作为脚本使用，用于分类处理其他以"YYmmdd"日期信息作名称开头的目录或文件。
### tar_gzip.py 
tar_gzip.py 是一个批量打包模块，为 nginx 日志备份目录提供后续的批量压缩处理功能，本模块主要使用的也是 Python3 的 os 模块。打包压缩的格式是 \*.tar.gz，可根据实际需求修改，新生成的打包压缩文件会存放在原来目标文件所在目录中。可配合 crontab 定时任务使用，定期对 nginx 日志备份目录进行自动打包压缩。本模块也可单独作为脚本使用，用于批量打包压缩其他目录或文件。
 
## 项目软件环境及使用说明
### 软件环境
项目软件环境：linux 和 python3</br>
其中 linux 涉及定时任务 crontab，python3 涉及到包管理工具 pip3</br>
### Nginx 日志分割备份模块 nginx_log_backup.py 使用方法 
下载本项目到任意目录后，根据实际nginx的 nginx.conf 配置文件的设置情况，修改 nginx_log_backup.py 内容。
```
 # 根据实际路径修改变量内容
    nginx_path = '/usr/local/webserver/nginx' # nginx 目录绝对路径
    nginx_log_path = nginx_path + '/logs' # nginx 的日志存储路径
    nginx_logs_filename = ['access.log','host.access.log',\
                           'error.log','monitor.access.log']  # 要备份的 log 文件名
    nginx_logs_backup_path = '/usr/local/webserver/nginx/backuplogs'  # 备份文件目的路径
    nginx_pid_path = nginx_log_path +'/' +'nginx.pid'  # Nginx.pid 文件的路径
```
修改好后保存，设置 linux 定时任务，让脚本定时自动执行。</br>
由于分片和备份 nginx log 文件需要 root 权限，但过程中又不能手动执行 sudo 和输入密码，所以定时任务需要挂在 root 名下。</br>
```
$ pwd
/home/sunnylinux/useful_script/python3_script/nginx_log_backup
$ whereis python3
python3: /usr/bin/python3 /usr/local/python3
$ sudo crontab -e
[sudo] sunnylinux 的密码：
no crontab for root - using an empty one
crontab: installing new crontab
```
crontab 文件中添加以下一句，表示每天凌晨两点三十五自动以 root 权限执行日志分片备份脚本
```
35 02 * * * /usr/bin/python3 /home/sunnylinux/useful_script/python3_script/nginx_log_backup/nginx_log_backup.py
```
查看是否已设置好crontab
```
$ sudo crontab -l
35 02 * * * /usr/bin/python3 /home/sunnylinux/useful_script/python3_script/nginx_log_backup/nginx_log_backup.py
```
注意：设置 crontab 必须要 sudo，这样才能在自启过程中使用root权限，不sudo会设置在一般用户名下
```
$ sudo tail -f /var/log/cron
Jan 30 02:35:01 centOSlearning CROND[5896]: (root) CMD (/usr/bin/python3 /home/sunnylinux/useful_script/python3_script/nginx_log_backup/nginx_log_backup.py )
```
可以看到定时任务已经成功执行，查看一下备份文件目录
```
$ pwd
/usr/local/webserver/nginx/backuplogs
$ ls
20190129_backup_logs  20190130_backup_logs
$ cd ./20190130_backup_logs/
$ ls
20190130_022048_access.log       20190130_022048_monitor.access.log  20190130_023501_host.access.log
20190130_022048_error.log        20190130_023501_access.log          20190130_023501_monitor.access.log
20190130_022048_host.access.log  20190130_023501_error.log
```
20190130_023501_monitor.access.log 看到这个编号的备份文件，则脚本自动定时执行成功。</br>
其余编号开头为当天手动执行脚本所产生的分片备份log文件。</br>
```
$ cat 20190130_022048_monitor.access.log
192.168.137.1 - - [30/Jan/2019:01:43:47 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:01:43:51 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:01:43:51 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:01:43:51 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:01:43:52 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:45 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:45 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:46 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:46 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:46 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
192.168.137.1 - - [30/Jan/2019:02:19:48 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"


$ cat 20190130_023501_monitor.access.log
192.168.137.1 - - [30/Jan/2019:02:28:45 +0800] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" "-"
```
注意：</br>
其实最好把脚本执行时间设置为每晚的23:59分，这样日志分割出来每份都包含当天完整的日志数据，比较容易做后续的统计分析。
```
# 修改 crontab 定时时间为每晚的23:59分
59 23 * * * /usr/bin/python3 /home/sunnylinux/useful_script/python3_script/nginx_log_backup/nginx_log_backup.py
```
### 目录文件日期分类模块 files_classifier.py 使用方法
前面介绍的 Nginx 日志分割备份模块用久了之后可能会产生一个问题：如果长期不对该备份目录做处理，目录中会塞满以日为单位分类的备份日志目录，各种年份和月份的日志备份目录混在一起。这样非常不利于数据的整理收集而且手动分类效率非常低，所以需要一个可以自动将这些目录按年或月份分类整理的程序，本项目的 files_classifier.py 便实现了这一功能。</br> files_classifier.py 基本上能对任何以"YYmmdd"开头的文件或目录进行分类整理。</br>
![](https://github.com/dearxuany/Sharon_Technology_learning_note/blob/master/note_images/Linux_note_images/nginxlogs.png)
files_classifier.py 可以将上图这样的目录结构自动分类成下图这样的目录结构，让数据分类整理查找更加简单。
```
$ cd ./classfly_backuplogs/
[sunnylinux@centOSlearning classfly_backuplogs]$ tree
.
└── 2019_backup_logs
    ├── 201901_backup_logs
    │   ├── 20190129_backup_logs
    │   │   ├── 20190129_201940_access.log
    │   │   ├── 20190129_201940_error.log
    │   │   ├── 20190129_201940_host.access.log
    │   │   ├── 20190129_201940_monitor.access.log
    │   │   ├── 20190129_202242_access.log
    │   │   ├── 20190129_202242_error.log
    │   │   ├── 20190129_202242_host.access.log
    │   │   └── 20190129_202242_monitor.access.log
    │   ├── 20190130_backup_logs
    │   │   ├── 20190130_022048_access.log
    │   │   ├── 20190130_022048_error.log
    │   │   ├── 20190130_022048_host.access.log
    │   │   ├── 20190130_022048_monitor.access.log
    │   │   ├── 20190130_023501_access.log
    │   │   ├── 20190130_023501_error.log
    │   │   ├── 20190130_023501_host.access.log
    │   │   └── 20190130_023501_monitor.access.log
    │   └── 20190131_backup_logs
    │       ├── 20190131_023501_access.log
    │       ├── 20190131_023501_error.log
    │       ├── 20190131_023501_host.access.log
    │       └── 20190131_023501_monitor.access.log
    └── 201902_backup_logs
        └── 20190202_backup_logs
            ├── 20190202_021657_access.log
            ├── 20190202_021657_error.log
            ├── 20190202_021657_host.access.log
            └── 20190202_021657_monitor.access.log

7 directories, 24 files
```
files_classifier.py 提供按年分类和按月分类两种分类方法，可按照以下步骤设置：
```
# 修改函数 file_classfly(dirpath,classflypath,dirname)下的部分，不需要的模式注释掉即可
$ vim files_classifier.py

    # 按月分类
    year_dir_exists_test(year_mounth_dict)
    mounth_dir_exists_test(year_mounth_dict)
    move_files_mounth(dir_file_list)

    # 按年分类
    # year_dir_exists_test(year_mounth_dict)
    # move_files_year(dir_file_list)

```
#### 脚本模式
files_classifier.py 用法比较简单，只需要对分类目标文件所在目录、分类后的目的目录、分类后的目录名设置，便可使用。
```
$ vim files_classifier.py

# 作为脚本使用，修改以下部分
if __name__ == '__main__':
    dir_path = '/usr/local/webserver/nginx/backuplogs'  # 要分类的文件所在目录路径，此处设置的是 nginx_log_backup.py 指定的备份目录
    classfly_path = '/usr/local/webserver/nginx/classfly_backuplogs'  # 文件分类目的目录路径
    dir_name = '_backup_logs'  # 除日期以外部分的分类目录名称
```
在任意路径执行本脚本即可，也可配合 linux 的 crontab 定时任务来以一定时间间隔来让系统自动对备份目录进行分类
```
$ python3 files_classifier.py
```
#### 作为模块导入到 python 解释器使用
在 files_classifier.py 所在目录中启动 python 解释器并导入模块，设置分类目标文件所在目录、分类后的目的目录、分类后的目录名
```
>>> import files_classifier
>>> dir_path = '/home/sunnylinux/pythontest/python3_script/mk_file_test_mounth'
>>> classfly_path = '/home/sunnylinux/pythontest/python3_script/backuplog_classfly_mounth'
>>> dir_name = '_backup_logs'
>>> files_classifier.file_classfly(dir_path,classfly_path,dir_name) # 分类程序入口
```
### 批量打包模块 tar_gzip.py 使用方法
修改模块以下内容，tar_gzip(startpath)可选择压缩的模式：tar_first_dir(dir_list)批量压缩启动目录中的内容、tar_second_dir(dir_list)批量压缩启动目录中所有目录中的内容，要注意两者的区别，不使用的模式注释掉即可。使用前需要修改启动目录的路径，注意启动目录的位置，不然可能压缩错目标文件，需重新操作。注意，压缩文件会被放置在原路径且源文件不会被删除。</br>
在 nginx 分割备份的场景中，启动目录可填 nginx 的备份目录，根据需求直接按日压缩或者经过 files_classifier.py 分类后再进行按月压缩或按年压缩。
```
def tar_gzip(startpath):
    start_path = startpath
    dir_list = os.listdir(start_path)

    # 打包当前目录中的内容
    tar_first_dir(dir_list)

    # 打包当前目录中的目录的内容
    # tar_second_dir(dir_list)


if __name__ == '__main__':
    start_path = '/usr/local/webserver/nginx/classfly_backuplogs'  # 启动目录路径

    tar_gzip(start_path)
```
按年压缩效果，使用年分类及 tar_first_dir(dir_list) 模式
```
[sunnylinux@centOSlearning backuplog_classfly]$ ls
2016_backup_logs         2017_backup_logs         2018_backup_logs
2016_backup_logs.tar.gz  2017_backup_logs.tar.gz  2018_backup_logs.tar.gz
```
按月压缩效果，使用月分类及 tar_second_dir(dir_list) 模式
```
[sunnylinux@centOSlearning backuplog_classfly_mounth]$ ls
2017_backup_logs  2018_backup_logs
[sunnylinux@centOSlearning backuplog_classfly_mounth]$ cd 2018_backup_logs/
[sunnylinux@centOSlearning 2018_backup_logs]$ ls
201801_backup_logs         201805_backup_logs         201809_backup_logs
201801_backup_logs.tar.gz  201805_backup_logs.tar.gz  201809_backup_logs.tar.gz
201802_backup_logs         201806_backup_logs         201810_backup_logs
201802_backup_logs.tar.gz  201806_backup_logs.tar.gz  201810_backup_logs.tar.gz
201803_backup_logs         201807_backup_logs         201811_backup_logs
201803_backup_logs.tar.gz  201807_backup_logs.tar.gz  201811_backup_logs.tar.gz
201804_backup_logs         201808_backup_logs         201812_backup_logs
201804_backup_logs.tar.gz  201808_backup_logs.tar.gz  201812_backup_logs.tar.gz
```
