# Connection_monitor
业务系统连接状态监控告警
## 功能
* 域名可用性检测、域名解析正确性检测、dns 可用性检测、url 响应速度性能检测、内外网联通性检测。
* 单次请求结果输出 json 格式，后期接入 elk 做可视化解析，请求失败原因输出到日志文件，方便问题排查。
* 部署位置：阿里云及办公网 ansible 主机各一个
### 检测逻辑
TCP 请求建立连接 ConnectTimeout 3 秒，响应readTimeout 5 秒，单次请求建立连接尝试 3 次，如果 3 尝试都失败那判断这次请求失败，各项输出为 none。
```
{
	"timestamp": "2019-12-24 06:52:51.917570",
	"localhostName": "opd-sharonli-01",
	"localhostIP": "192.168.126.129",
	"hostIP": "14.215.177.39",
	"dnsServerList": ["10.0.0.51", "10.0.0.52"],
	"url": "https://www.baidu.com",
	"statusCode": 200,
	"requestTime": 0.052767,
	"result": "success"
}
```
如果请求成功，即有状态码输出，则计算响应时间。</br>
10 次请求算响应均值和标准差，请求成功率低于 0.7 告警，响应均值低于 5 秒告警。</br>
```
{
	"timestamp": "2019-12-24 06:52:51.611699",
	"url": "https://www.baidu.com",
	"hostList": ["14.215.177.39", "14.215.177.38"],
	"dnsServerList":["10.0.0.51", "10.0.0.52"],
	"checkTimes": 10,
	"checkDelta": 1,
	"requestStatus": [200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
	"requestSpendTime": [0.036415, 0.033601, 0.052242, 0.056756, 0.045676, 0.029547, 0.042732, 0.030582, 0.053056, 0.063011],
	"localhostName": "opd-sharonli-01",
	"localhostIP": "192.168.126.129",
	"requestSuccessPerc": 1.0,
	"requestTimeMean": 0.044,
	"requestTimeStd": 0.011,
	"triggerStatus": "域名请求正常"
}
```

### 检测样例
* 快速响应要求高系统（如问答机器人）响应慢，返回信息延迟状况，部分请求超时
* 系统后端集群故障导致 502 无法响应请求
* 请求被 waf 拦截，响应失败

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
# 监控项导入目录
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

