# python_program
* Python3 实现定时监控 linux 系统性能并发送邮件通知</br>
https://github.com/dearxuany/python_program/tree/master/Linux_monitor_send_email </br>
本项目主要使用 Python3 的三个开源模块 psutil、jinja2、yagmail 并配合 linux 系统自带的 crontab 定时任务，来实现对 linux 系统性能数据的定时采集、数据格式调整、自动发送到指定邮箱的功能，采集内容包括：开机时间，当前主机名、当前采集时间、CPU个数、CPU使用率、内存总量、内存利用率、内存已用空间、内存可用空间、磁盘总量、磁盘利用率、磁盘已用空间、磁盘可用空间。整个功能实现过程完全自动化，免除了人工手动收集数据、汇总整理、发送的繁琐过程，充分提高了任务完成效率和数据可靠性。</br>
</br>

* Python3 实现 linux 终端界面发信息到微信</br>
https://github.com/dearxuany/python_program/tree/master/Linux_monitor_send_wechat </br>
本项目主要使用 Python3 的 wxpy 微信个人号 API 模块，配合 psutil 模块实现 linux 系统的性能数据采集并直接在 linux 终端发送到个人微信账号或微信群。本项目从数据传入到微信发送信息到用户或微信群，整个过程仅依靠 linux 终端完成，不需要额外的图形化界面，简化了从 linux 提取信息再发送到微信的各种繁琐步骤；程序使用交互形式编写，对 wxpy 微信个人 API 模块进行了封装，不需要每次使用都修改代码，只需在命令行界面完成发送对象的选取即可实现发送微信的功能，提高了程序的易用性。</br>
</br>
