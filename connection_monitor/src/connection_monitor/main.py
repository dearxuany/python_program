#! /usr/bin/env python3

import os
import sys
import imp
from get_url_request import url_connection_monitor



def load_conf():
    mainDir=os.path.dirname(os.path.abspath(__file__))
    baseDirList=mainDir.split("/")[0:-2]
    baseDir="/".join(baseDirList)
    confDir=baseDir+"/config/conf.py"
    conf=imp.load_source("conf",confDir)
    return conf

def main():
    conf=load_conf()
   
    # 获取域名检测配置
    urlcheckConf=conf.urlcheck_config_info()
    if urlcheckConf["urlcheck"] == "True":
        url_connection_monitor(urlcheckConf)
    else:
        pass
    return


if __name__=="__main__":
    main()

