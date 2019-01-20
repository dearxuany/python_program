# python_program
* linux 系统性能定时监控并发送邮件通知</br>
https://github.com/dearxuany/python_program/tree/master/Linux_monitor_send_email </br>
本项目主要使用 Python3 的三个开源模块 psutil、jinja2、yagmail 并配合 linux 系统自带的 crontab 定时任务，来实现对 linux 系统性能数据的定时采集、数据格式调整、自动发送到指定邮箱的功能，采集内容包括：开机时间，当前主机名、当前采集时间、CPU个数、CPU使用率、内存总量、内存利用率、内存已用空间、内存可用空间、磁盘总量、磁盘利用率、磁盘已用空间、磁盘可用空间。
