# gitanalysis
git 项目代码提交分析工具，用于统计公司所有业务系统每周 git 代码变更状况，内容包括： 日期、项目名称、成员名称、commit次数、新增行数、删除行数、变更行数。</br>

每周在本周版本上线后，获取各项目 master 分支提交信息，结果以 json 格式输出到 logstach 进行分词，elasticsearch 作数据存储，使用 kibana 分析展示。</br>

## 依赖
代码管理 git</br>

语言环境 python3/pip3/virtualenv</br>

定时任务 crontab</br>

数据采集分析 filebeat/logstash/elasticsearch/kibana</br>

## 程序部署
下载源码
```
git clone 项目仓库链接
```
初次部署需构建新的项目运行虚拟环境
```
mkdir -p /sdata/app/pythonVenv
cd /sdata/app/pythonVenv
python3 -m virtualenv .gitanalysis_venv
```
进入项目目录按实际路径激活虚拟环境
```
. ./bin/venv_activate.sh
```
虚拟环境中安装项目依赖模块
```
pip3 install -r requirement.txt
```
进入项目目录,进行参数配置
```
# vim code/main.py

    # 目标分析代码目录
    destCodeDir="/sdata/app/gitAnalysis/destCode"
    # 手动导入代码仓库链接配置
    gitRepositoryHttps="/sdata/app/gitAnalysis/docs/gitRepositoryHttps.txt"
    # 分析结果导出目录
    resultsDir="/sdata/app/gitAnalysis/results"
    # 分析时间跨度
    timeDelta=7

    # 敏感信息请勿丢失及泄露
    gitlab_url = "https://git.domainname.com"
    gitlab_token = "按 gitlab 实际生成 token 配置"

    # 是否自动导入 gitlab 中最新代码仓库
    autoGetNewProjects=True

```
在虚拟环境激活的状态下查找 python3 路径
```
(.gitanalysis_venv) [snail@alihn1-opd-jenkins-01 gitanalysis]$ which python3
/sdata/app/pythonVenv/.gitanalysis_venv/bin/python3
```
使用以上绝对路径设置 crontab 定时任务
```
crontab -e
# gitlab code analysis
0 1 * * 1 /sdata/app/pythonVenv/.gitanalysis_venv/bin/python /sdata/app/gitAnalysis/gitanalysis/code/main.py
```
