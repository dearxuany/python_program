# python_program
* Python3 实现定时监控 linux 系统性能并发送邮件通知</br>
https://github.com/dearxuany/python_program/tree/master/Linux_monitor_send_email </br>
本项目主要使用 Python3 的三个开源模块 psutil、jinja2、yagmail 并配合 linux 系统自带的 crontab 定时任务，来实现对 linux 系统性能数据的定时采集、数据格式调整、自动发送到指定邮箱的功能，采集内容包括：开机时间，当前主机名、当前采集时间、CPU个数、CPU使用率、内存总量、内存利用率、内存已用空间、内存可用空间、磁盘总量、磁盘利用率、磁盘已用空间、磁盘可用空间。整个功能实现过程完全自动化，免除了人工手动收集数据、汇总整理、发送的繁琐过程，充分提高了任务完成效率和数据可靠性。</br>
</br>

* Python3 实现 linux 终端界面发信息到微信</br>
https://github.com/dearxuany/python_program/tree/master/Linux_monitor_send_wechat </br>
本项目主要使用 Python3 的 wxpy 微信个人号 API 模块，配合 psutil 模块实现 linux 系统的性能数据采集并直接在 linux 终端发送到个人微信账号或微信群。本项目从数据传入到微信发送信息到用户或微信群，整个过程仅依靠 linux 终端完成，不需要额外的图形化界面，简化了从 linux 提取信息再发送到微信的各种繁琐步骤；程序使用交互形式编写，对 wxpy 微信个人 API 模块进行了封装，不需要每次使用都修改代码，只需在命令行界面完成发送对象的选取即可实现发送微信的功能，提高了程序的易用性。</br>
</br>

* Python3 实现 NginX 日志定时切分备份、日期分类、批量压缩</br>
https://github.com/dearxuany/python_program/blob/master/Nginx_log_backup </br>
本项目主要使用 Python3 自带的 os 模块和 time 模块，配合 linux 的 crontab 定时任务以及借助 Nginx 本身的一些特性，来实现对 Nginx logs 文件的定时自动切分和备份功能。除此之外，本项目还利用了 Pyhton3 的 os 模块来实现了对备份目录的大批量日期分类、压缩功能，为后续的备份目录处理提供方便。日志切分备份模块适用于定时自动切分备份与特殊状况下的人手执行脚本切分备份，自动和手动在切分备份逻辑上不会起冲突，无需增加目录或改名等额外操作，适用于多种切分备份场景，减少重复的手工操作，降低误操作致数据丢失的概率；日期分类模块可按年或月份来对 nginx 备份目录进行分类，可自动且快速地将以"YYmmdd"日期信息作名称开头的目录或文件进行按年份或月份进行分类，分类脚本适用于多种场景，方便高效；批量压缩模块能批量对目录或文件进行压缩处理，除了能压缩当前目录中的所有目录外，还可选压缩当前目录的子目录中的内容，免去逐个手动遍历各个目录再进行压缩的繁琐过程，大大降低时间成本。</br>
