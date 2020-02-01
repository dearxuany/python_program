#! /usr/bin/env python3

import socket
import requests
from requests.adapters import HTTPAdapter
from time import sleep
from datetime import datetime
import os
import numpy as np
from json import dumps
from data_format import get_format
from get_results import results_output
from  input_readline import read_file_lines
from send_dingtalk import sendData

def localhost_info():
    localhostName=socket.gethostname()
    localhostIP=socket.gethostbyname(localhostName)
    return dict(localhostName=localhostName,localhostIP=localhostIP)

def request_info(timestamps,logDir,logName,url):
    s=requests.Session()
    s.mount('http://',HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    
    try:
        r=s.get(url=url,timeout=(3,5))
    except requests.exceptions.RequestException as e:
        results_output(logDir,logName,timestamps+" "+str(e))
        statusCode=None
        requestTime=None
        result="ConnectionError"
    else:
        statusCode=r.status_code
        requestTime=r.elapsed.total_seconds()
        result="success"
    finally:
        s.close()
        return dict(url=url,statusCode=statusCode,requestTime=requestTime,result=result)


def url_dns_info(logDir,logName,timestamps,url):

    try:
        hostIP=socket.gethostbyname(url.split("/")[2])
    except socket.error as e:
        results_output(logDir,logName,timestamps+" "+str(e))
        hostIP=None
        
    dnsServerIP=os.popen('cat /etc/resolv.conf|grep nameserver|awk \'{print $2}\'').read()
    dnsServerList=dnsServerIP.split()
    return dict(hostIP=hostIP,dnsServerList=dnsServerList)


def check_url(resultsDir,checkTimes,checkDelta,logDir,logName,url,localhostInfo):
    hostList=[]
    requestStatus=[]
    requestSpendTime=[]

    for n in range(0,checkTimes):
        urlInfoDict={}
        urlInfoDict["timestamp"]=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        urlInfoDict.update(localhostInfo)
        IPInfo=url_dns_info(logDir,logName,urlInfoDict["timestamp"],url)
        urlInfoDict.update(IPInfo)
        urlInfoDict.update(request_info(urlInfoDict["timestamp"],logDir,logName,url))
        hostList.append(urlInfoDict["hostIP"])
        requestStatus.append(urlInfoDict["statusCode"])
        requestSpendTime.append(urlInfoDict["requestTime"])
        sleep(checkDelta)
        results_output(resultsDir,"urlInfo.txt",str(dumps(urlInfoDict,ensure_ascii=False)))
    return dict(timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),url=url,hostList=list(set(hostList)),dnsServerList=IPInfo["dnsServerList"],checkTimes=checkTimes,checkDelta=checkDelta,requestStatus=requestStatus,requestSpendTime=requestSpendTime)

def data_calculation(urlCheckInfo):
    requestSuccessNum=0
    for n in range(len(urlCheckInfo["requestStatus"])):
        if urlCheckInfo["requestStatus"][n] is not None and urlCheckInfo["requestStatus"][n] < 404:
            requestSuccessNum=requestSuccessNum+1
    urlCheckInfo["requestSuccessPerc"]=requestSuccessNum/len(urlCheckInfo["requestStatus"])

    requestSpendTimeList=[]
    for n in range(len(urlCheckInfo["requestSpendTime"])):
        if urlCheckInfo["requestSpendTime"][n] is not None:
            requestSpendTimeList.append(urlCheckInfo["requestSpendTime"][n])
    if len(requestSpendTimeList) > 0:
        urlCheckInfo["requestTimeMean"]=round(np.mean(requestSpendTimeList),3)
        urlCheckInfo["requestTimeStd"]=round(np.std(requestSpendTimeList),3)
    else:
        urlCheckInfo["requestTimeMean"]=None
        urlCheckInfo["requestTimeStd"]=None

    return urlCheckInfo

def send_dingtalk_msg(triggerTplDir,urlStatisticData,sendURL,atUser,msgtype):
    msgData=get_format(triggerTplDir,**urlStatisticData)
    typeValue={}
    if msgtype=="text":  
        typeValue[msgtype]=dict(title="域名监控",content=msgData)
    sendData(sendURL,atUser,msgtype,typeValue)
    

def url_connection_monitor(urlcheckConf):

    inputFileDir=urlcheckConf["inputfiledir"]+"/"+urlcheckConf["inputfile"]
    resultsDir=urlcheckConf["resultsdir"]
    triggerTplDir=urlcheckConf["triggertpldir"]+"/"+urlcheckConf["triggertplfile"]
    logDir=urlcheckConf["logdir"]
    logName=urlcheckConf["logfile"]

    checkTimes=int(urlcheckConf["checktimes"])
    checkDelta=int(urlcheckConf["checkdelta"]) 
    triggerPerc=float(urlcheckConf["triggerperc"])
    triggerRequestTime=int(urlcheckConf["triggerrequesttime"])
    
    sendURL=urlcheckConf["sendurl"]
    atUser=urlcheckConf["atuser"].split(",")
    msgtype=urlcheckConf["msgtype"]   



    urlList=read_file_lines(inputFileDir)
    print(urlList)
    localhostInfo=localhost_info()
    for n in range(len(urlList)):
        url=urlList[n]
        urlCheckInfo=check_url(resultsDir,checkTimes,checkDelta,logDir,logName,url,localhostInfo)
        urlCheckInfo.update(localhostInfo)
        urlStatisticData=data_calculation(urlCheckInfo)
        if urlStatisticData["requestSuccessPerc"] < triggerPerc:
            urlStatisticData["triggerStatus"]="域名请求失败"
            send_dingtalk_msg(triggerTplDir,urlStatisticData,sendURL,atUser,msgtype)
        elif urlStatisticData["requestTimeMean"] > triggerRequestTime:
            urlStatisticData["triggerStatus"]="域名响应慢"
            send_dingtalk_msg(triggerTplDir,urlStatisticData,sendURL,atUser,msgtype)
        else:
             urlStatisticData["triggerStatus"]="域名请求正常"
        results_output(resultsDir,"urlStatistic.txt",str(dumps(urlStatisticData,ensure_ascii=False)))

