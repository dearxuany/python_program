# Connection_monitor

业务系统连接状态监控告警

## 部署
### 环境配置
软件依赖
```
python3/pip3/virtualenv/crontab/dingtalk
```
初次部署需构建新的项目运行虚拟环境
```
mkdir -p /sdata/app/pythonVenv
cd /sdata/app/pythonVenv
virtualenv -p python3 .connection_monitor_venv
```
代码仓库克隆
```
git clone git@git.*****.com:****/connection_monitor.git
```
进入项目目录按实际路径激活虚拟环境
```
. ./bin/venv_activate.sh
```
虚拟环境中安装项目依赖模块
```
pip3 install -r requirement.txt
```

### 链接监控接入配置
配置文件
```
# vim config/conf.ini 
[public]
# url导入目录
inputFileDir=/sdata/app/connection_monitor/docs
# 结果导出目录
resultsDir=/sdata/data/connection_monitor
# 渲染模板目录
triggerTplDir=/sdata/app/connection_monitor/docs/template
logDir=/sdata/var/log/connection_monitor

[dingtalk]
# prd robot
#sendURL=https://oapi.dingtalk.com/robot/send?access_token=123454
# dev robot
sendURL=https://oapi.dingtalk.com/robot/send?access_token=5667688
atUser = 
msgtype=text

[urlcheck]
# 是否开启 url 监控功能
urlCheck=True
# url 导入文档
inputFile=urlInput.txt
# 渲染模板文件
triggerTplFile=urlTrigger.tpl
logFile=urlRequest.log
# 检测次数
checkTimes=10
# 检测时间间隔
checkDelta=1
# 触发成功率
triggerPerc=0.7
# 超时等待时间
triggerRequestTime=5

```
监控 url 设置
```
# vim docs/urlInput.txt 
https://www.baidu.com/
https://www.google.com/
https://cn.bing.com/
https://github.com/

```
### crontab 激活虚拟环境执行程序
在虚拟环境激活的状态下查找 python3 路径
```
(.connection_monitor_venv) $ which python3
/sdata/app/pythonVenv/.connection_monitor_venv/bin/python3
```
使用以上绝对路径设置定时任务
```
crontab -e
*/10 * * * * /sdata/app/pythonVenv/.connection_monitor_venv/bin/python3 /sdata/app/connection_monitor/src/connection_monitor/main.py
```


## 常见问题
### pip 源变更
若出现安装模块超时，需将 pip 源调整为国内源，此处调整为清华源
```
mkdir ~/.pip
vim ~/.pip/pip.conf
```
编辑文档
```
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### virtualenv 路径无法找到
可使用以下命令替代
```
python3 -m virtualenv .connection_monitor_venv
```

