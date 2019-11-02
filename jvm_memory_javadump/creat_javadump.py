#! /usr/bin/python3

import os
import time


def getTime():
    date = time.strftime("%Y%m%d", time.localtime())
    dumpTime = time.strftime("%H%M%S", time.localtime())
    return dict(date=date,dumpTime=dumpTime)


def getPid(processName):
    ps=os.popen("ps -ef|grep {}|grep -v grep".format(processName)).read().split("     ")
    return dict(user=ps[0],pid=ps[1])


def createJavadump(javaDumpdir,processName,datetime,user,pid):
    javaDumpName="{}/javadump_{}_{}_{}".format(javaDumpdir,processName,datetime["date"],datetime["dumpTime"])
    os.system("su - {} -c 'jmap -dump:format=b,file={} {}'".format(user,javaDumpName,pid))
    return javaDumpName




def tarJavadump(javaDumpName):
    javaDumpTar=javaDumpName+".tar.gz"
    os.system("tar -cvz -f {} {}".format(javaDumpTar,javaDumpName))
    return javaDumpTar


def sendCMD(keyDir,sendFileName,destUser,destHost,destDir,crondShellDir):
    scpCMD="scp -P 9900 -i {} {} {}@{}:{}".format(keyDir,sendFileName,destUser,destHost,destDir)
    os.system("echo '#! /bin/bash'> {}".format(crondShellDir))
    os.system("echo {}>> {}".format(scpCMD,crondShellDir))
    return


def setCrontab(crondShellDir,user):
    sendDay="0"+str(int(time.strftime("%d", time.localtime())[1])+1)
    sendMounth=time.strftime("%m", time.localtime())
    os.system("echo '30 05 {} {} * /bin/bash {}'>> /var/spool/cron/{}".format(sendDay,sendMounth,crondShellDir,user))
    return



if __name__=="__main__":
    processName="tomcat"
    javaDumpdir="/sdata/javadump"
    keyDir="/sdata/javadump/scp_key"
    destHost="localhost.*****.net"
    destUser="****"
    destDir="/data2/log/prd/bnail/"
    crondShellDir="/sdata/javadump/scp_send.sh"

    datetime={}
    psDict={}


    psDict=getPid(processName)
    datetime=getTime()
    javaDumpName=createJavadump(javaDumpdir,processName,datetime,psDict["user"],psDict["pid"])
    javaDumpTar=tarJavadump(javaDumpName)
    sendCMD(keyDir,javaDumpTar,destUser,destHost,destDir,crondShellDir)
    setCrontab(crondShellDir,psDict["user"])
