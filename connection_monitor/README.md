# Connection_monitor

业务系统连接状态监控告警

## 软件依赖
python3 及 pip3

## 虚拟环境构建
初次部署需构建新的项目运行虚拟环境
```
mkdir -p /sdata/app/pythonVenv
cd /sdata/app/pythonVenv
virtualenv -p python3 .connection_monitor_venv
```

## 代码仓库克隆
```
git clone git@git.*****.com:****/connection_monitor.git
```

## 激活虚拟环境
进入项目目录按实际路径激活虚拟环境
```
. ./bin/venv_activate.sh
```

## 虚拟环境中安装项目依赖模块
```
pip3 install -r requirement.txt
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
