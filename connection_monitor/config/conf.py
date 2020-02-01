#! /usr/bin/env python3

import configparser
import os

def get_conf_path():
    confBaseDir=str(os.path.dirname(os.path.dirname(__file__)))+'/config'
    return confBaseDir

def load_config_info(confKey):
    confPath=get_conf_path()+'/conf.ini'

    cf = configparser.ConfigParser()
    cf.read(confPath)
   
    configPara=cf._sections[confKey]

    return dict(configPara)

def public_config_info():
    publicPara=load_config_info("public")
    return publicPara

def dingtalk_config_info():
    publicPara=public_config_info()
    dingtalkPara=load_config_info("dingtalk")

    dingtalkFullPara=publicPara.copy()
    dingtalkFullPara.update(dingtalkPara)

    return dingtalkFullPara

def urlcheck_config_info():
    dingtalkPara=dingtalk_config_info()
    checkurlPara=load_config_info("urlcheck")

    checkurlFullPara=dingtalkPara.copy()
    checkurlFullPara.update(checkurlPara)

    return checkurlFullPara
