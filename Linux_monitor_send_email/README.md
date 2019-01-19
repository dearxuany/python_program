# Python3 对 linux 系统进行性能监控并发送邮件通知
## 项目介绍
现实工作中，定时收集并监控服务器 linux 系统各项性能指标并发送邮件给个相关管理人员是一个非常常见而实用的应用需求。
无论是过去还是现在，很多管理人员会使用 SHELL 来编写监控程序，但随着行业的发展 Python 也因为其简洁、可读性高、丰富的库资源而逐渐成为维护人员的另一种常用工具。</br>
</br>
本项目主要使用 Python3 的三个开源模块 psutil、jinja2、yagmail 并配合 linux 系统自带的 crontab 定时任务，来实现对 linux 系统性能数据如CPU、内存、磁盘等相关信息的定时采集、格式调整、发送到相关维护人员邮箱的功能。</br>
本项目主要有以下几个特点：
* 使用 Python3 中的 psutil 模块来采集整合系统的各项性能指标，简化了使用 SHELL 来获取并整合系统监控信息的复杂度；
* 使用 Python3 中的 jinja2 渲染模板来对采集到的信息进行格式的调整，让性能数据的显示更直观、有更高的可读性；
* 使用 Python3 中的 yagmail 邮件模块来实现性能数据发送到邮箱的功能，除使用公司内部企业邮箱外还可使用现有的邮箱服务提供商的邮箱且易于更换，支持多个收件人同时接收数据；
* 项目整体使用 Python 编写，比 SHELL 更加简短，可读性强，更加易于后期维护。

## 项目结构与功能说明
```
Linux_monitor_send_email
   ├── linux_monitor_send_email
   │   ├── data_format.py
   │   ├── __init__.py
   │   ├── main.py
   │   ├── monitor_data_collect.py
   │   ├── monitor.html
   │   └── send_email.py
   ├── README.md
   └── requirements.txt
```
目录 ./linux_monitor_send_email 中存放项目代码，requirements.txt 标有本项目的外部 Python 包列表，README.md 为项目使用说明。
* main.py</br>
main.py 为本项目程序入口，该模块主要负责调用性能数据采集模块 monitor_data_collect.py 采集linux的实时性能数据，之后将采集模块的返回值传送给模板渲染模块 data_format.py 进行数据的格式调整，最后将格式调整后的数据传送给邮件发送模块 send_email.py 来进行邮件的发送。另外，该模块还承担邮件服务器 host 的设置、发件邮箱地址与密码的输入设置、收件邮箱地址的设置任务。
* monitor_data_collect.py </br>
monitor_data_collect.py 为本项目的系统性能数据采集模块。该模块负责调用 python 的 psutil 模块实时采集 linux 系统的性能数据，其中包括CPU个数、CPU使用率、内存总量、内存利用率、内存已用空间、内存可用空间、磁盘总量、磁盘利用率、磁盘已用空间、磁盘可用空间、开机时间，调用 socket 模块获得当前主机名，调用 time 模块获得当前采集时间。采集完成后，该模块会将性能数据保存在一个字典中并返回给 main.py。
* data_format.py </br>
data_format.py 为本项目的模板渲染模块，主要调用了 python 中的 jinja2 模块，通过 jinja2 模块使用 monitor.html 中格式来渲染性能数据，该模块负责对性能数据进行格式调整以达到便于人员阅读的效果。
* send_email.py </br>
send_email.py 为本项目的邮件发送模块，该模块主要调用了 python 的 yagmail 模块，负责将调整好格式的性能数据发送到指定邮箱之中。该模块还调用了 python 的 time 模块自动将发邮件的时间信息包含在邮件的标题中，便于阅读分类的同时防止被邮件服务商识别为垃圾邮件。
