# python_program
* Python3/logstash/elasticsearch/kibana 业务系统 git 提交分析工具</br>
https://github.com/dearxuany/python_program/tree/master/gitanalysis </br>
用于统计公司所有业务系统每周 git 代码变更状况，内容包括： 日期、项目名称、成员名称、commit次数、新增行数、删除行数、变更行数。每周在本周版本上线后，获取各项目 master 分支提交信息，结果以 json 格式输出到 logstach 进行分词，elasticsearch 作数据存储，使用 kibana 分析展示。</br>

* Python3 域名可用性监控</br>
https://github.com/dearxuany/python_program/tree/master/connection_monitor
域名可用性检测、域名解析正确性检测、dns 可用性检测、url 响应速度性能检测、内外网联通性检测。单次请求结果输出 json 格式，后期接入 elk 做可视化解析，请求失败原因输出到日志文件，方便问题排查。告警触发后调用钉钉机器人发送告警信息。

* Python3 读取 excel 信息批量生成 elasticsearch Xpack 用户及角色权限 </br>
https://github.com/dearxuany/python_program/tree/master/elasticsearch_user_migration </br>
用户信息记录于 xls 的 excel 中，使用 xlrd 读取 excel 中的用户信息存于字典，调整为 elasticsearch 可读取的 json 格式，使用 curl 调用 es 的 /_security/user API 生成用户及角色权限。

* Python3 生成 jvm 内存分析 javadump 文件并定时使用 scp 回传本地服务器</br>
https://github.com/dearxuany/python_program/tree/master/jvm_memory_javadump </br>
使用 jmap 生成 java 进程 javadump 二进制文件，用于分析 java 系统的 jvm 内存使用状况。一般情况下，生成的 javadump 二进制文件较大且不易切割解析，故需压缩发送。压缩完毕后，压缩文件依然会有 1GB 以上大小，从阿里云生产网络传输回本地内网需占用生产带宽，故须在深夜用户量较少时传输。执行过程：获取 java 进程当前 pid 及用户 - 根据当前时间使用 jmap 生产 javadump文件 - 压缩 - 生成 scp 回传脚本 - 设置 crontab 为第二天早上 5:30 回传 javadump 文件到本地服务器。

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
本项目主要使用 Python3 自带的 os 模块和 time 模块，配合 linux 的 crontab 定时任务以及借助 Nginx 本身的一些特性，来实现对 Nginx logs 文件的定时自动切分和备份功能。除此之外，本项目还利用了 Python3 的 os 模块来实现了对备份目录的大批量日期分类、压缩功能，为后续的备份目录处理提供方便。日志切分备份模块适用于定时自动切分备份与特殊状况下的人手执行脚本切分备份，自动和手动在切分备份逻辑上不会起冲突，无需增加目录或改名等额外操作，适用于多种切分备份场景，减少重复的手工操作，降低误操作致数据丢失的概率；日期分类模块可按年或月份来对 nginx 备份目录进行分类，可自动且快速地将以"YYmmdd"日期信息作名称开头的目录或文件进行按年份或月份进行分类，分类脚本适用于多种场景，方便高效；批量压缩模块能批量对目录或文件进行压缩处理，除了能压缩当前目录中的所有目录外，还可选压缩当前目录的子目录中的内容，免去逐个手动遍历各个目录再进行压缩的繁琐过程，大大降低时间成本。</br>
