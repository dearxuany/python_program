# Python3 实现 linux 终端界面发信息到微信
## 项目介绍
现实系统维护场景中，经常会出现要求将系统的性能监控信息及告警信息发送到邮箱等类似需求。
随着微信的应用越发广泛和商业化，还有需求提出想把 linux 系统上的一些性能、告警、日志等信息直接发送到各方人员的微信账号或微信群以便查看。</br>
</br>
现阶段 python3 应用广泛的微信 API 模块有 itchat 和 wxpy。 
wxpy 是在 itchat 的基础上，通过大量接口优化提升了模块的易用性，并进行丰富的功能扩展，所以 wxpy 的使用会比 itchat 更为广泛一些。</br>
</br>
事实上，在系统监控告警场景中，微信监控告警虽然是可实现的，但相对于邮件告警还是有一定劣势。
因为现行的 Python 微信相关模块在实现信息发送功能前都必须有一个手机扫码登录的过程，
wxpy 模块提供了一个缓存功能以解决一段时间内需要重复扫码登录的问题，但这个缓存时间依然是比较短，无法满足长时间的监控需求。</br>
</br>
在定时监控采集服务器性能数据的场景中，微信相对于邮件会有一定劣势，但微信在发送即时信息、减少人员沟通成本上依然有着绝对的优势，所以在 linux 终端环境实现微信消息的直接发送是非常有实用价值的，适用于各种需要将 linux 系统当前状态信息发送给外部人员以促进沟通合作、快速解决问题的场景。</br>
</br>
本项目主要使用 Python3 的 wxpy 微信个人号 API 模块，配合 psutil 模块实现 linux 系统的性能数据采集并直接在 linux 终端发送到个人微信账号或微信群。</br>
本项目有以下几个主要特点：</br>
* 从数据传入到微信发送信息到用户或微信群，整个过程仅依靠 linux 终端完成，不需要额外的图形化界面，简化了从 linux 提取信息再发送到微信的各种繁琐步骤；
* 程序使用交互形式编写，对 wxpy 微信个人 API 模块进行了封装，不需要每次使用都修改代码，只需在命令行界面完成发送对象的选取即可实现发送微信的功能，提高了程序的易用性。
## 项目结构与功能说明
```
Linux_monitor_send_wechat
├── linux_monitor_send_wechat
│   ├── __init__.py
│   ├── main.py
│   ├── monitor_data_collect.py
│   └── send_wechat.py
├── README.md
└── requirements.txt
```
目录 ./linux_monitor_send_wechat 中存放项目代码，requirements.txt 标有本项目的外部 Python 包列表，README.md 为项目使用说明。
* main.py </br>
main.py 为本项目程序入口，该模块主要负责调用性能数据采集模块 monitor_data_collect.py 采集linux的实时性能数据，然后根据微信的显示特性对数据进行一些格式调整，增加可读性。最后，调用基于 wxpy 的 send_wechat.py 让用户登录微信、选定发送对象（微信个人用户或微信群）、发送信息到指定接收对象。
* monitor_data_collect.py </br>
monitor_data_collect.py 为本项目的系统性能数据采集模块。该模块负责调用 python 的 psutil 模块实时采集 linux 系统的性能数据，其中包括CPU个数、CPU使用率、内存总量、内存利用率、内存已用空间、内存可用空间、磁盘总量、磁盘利用率、磁盘已用空间、磁盘可用空间、开机时间，调用 socket 模块获得当前主机名，调用 time 模块获得当前采集时间。采集完成后，该模块会将性能数据保存在一个字典中并返回给 main.py。
* send_wechat.py </br>
send_wechat.py 为本项目的微信登录、发送对象选取、微信信息发送模块。该模块主要调用了 Python3 的 wxpy 模块，采用交互模式编写。用户只需要执行程序，扫描终端界面显示的二维码登录微信后，根据程序的输出提示， 选取发送对象（微信用户/微信群）、输入发送对象信息（微信用户：昵称、性别、城市/微信群：群名称），即可完成 linux 终端到微信的信息直接发送。
## 项目环境及使用方法
### 软件环境
项目软件环境：linux 和 python3</br>
其中 python3 涉及到包管理工具 pip3
### 使用方法
下载本项目程序到任意目录后，安装项目依赖的 python 包
```
$ pip3 install -r requirements.txt
```
直接执行 main.py
```
$ python3 main.py
```
程序会要求扫描二维码登录微信，如下图这个样子，用手机微信扫描二维码并确认登录</br>
![](https://github.com/dearxuany/Sharon_Technology_learning_note/blob/master/note_images/Python_note_images/linux_send_wechat_QR.png)</br>
注意：</br>
第一次登录过后，程序会生成一个 wxpy.pkl 文件，之后在一段时间内重复执行程序则不需要再重复扫码登录的步骤，程序自动登录微信。</br>
如果不需要自动登录，则可直接删除 wxpy.pkl 文件，重新启动程序后则会要求重新登录。</br>
```
# 看到这句表示登录成功，as 后面是当前登录微信的微信昵称
Login successfully as Xuan
```
扫码登录后，根据程序的输出提示选择微信发送对象，u 表示微信用户，g 表示微信群，推荐使用微信群发送信息。</br>
选择 u 即发送对象为用户，则会要求输入发送对象的微信昵称、性别、所在城市，其中仅有性别为可选：
```
Do you want to send massage to a wechat user or a wechat group?(u/g)u
Place input the nickname of the wechat user: Xuan
Place input the wechat user gender (MALE/FEMALE):
Place input the city of wechat user (example:广州):广州
Massage send to <Friend: Xuan>: OK!
```
选择 g 即发送对象为微信群，则仅需输入该微信群的群名：
```
Do you want to send massage to a wechat user or a wechat group?(u/g)g
Place input the groupname of the wechat group: testing
Massage send to <Group: testing>: OK!
```
看到最后一句 Massage send to <Group: testing>: OK! 则为发送成功。</br>
![](https://github.com/dearxuany/Sharon_Technology_learning_note/blob/master/note_images/Python_note_images/linux_send_wechat.jpg)

## send_wechat.py 的单独使用
在 send_wechat.py 所在目录中，启动 python3 解释器，导入 send_wechat
```
>>> import send_wechat
>>> send_wechat.send_massage('Can we talk??')
Do you want to send massage to a wechat user or a wechat group?(u/g)g
Place input the groupname of the wechat group: testing
Massage send to <Group: testing>: OK!
```
如果想在其他目录中也使用本模块，则可手动将本模块放置到 python3 解释器查找模块的默认路径中，
详情：[Python 模块](https://github.com/dearxuany/Sharon_Technology_learning_note/blob/master/python_note/Python%20%E6%A8%A1%E5%9D%97.MD)
