#！/usr/bin/python3

import xlrd
import os
from json import dumps


def set_es_user(username,userInfo):
    userInfoJson=dumps(userInfo,ensure_ascii=False)
    print(username)
    setUserCMD='curl --user elastic:yourpassword -H "Content-Type: application/json" -XPUT http://10.0.0.153:19200/_security/user/{} -d \'{}\''.format(username,userInfoJson)
    result=os.popen(setUserCMD).read()
    print(result)
    return


def read_excel(excel):
    workbook=xlrd.open_workbook(excel)
    sheet_name=workbook.sheet_names()[0]
    sheet=workbook.sheet_by_index(0)
    userInfo={}
    for rown in range(sheet.nrows):
        username=sheet.cell_value(rown,0)
        userInfo["full_name"]=sheet.cell_value(rown,1)
        userInfo["email"]=sheet.cell_value(rown,2)
        userInfo["password"]=sheet.cell_value(rown,3)
        userInfo["roles"]=["kibana_user","lians-log-read","bnail-log-read","micros-log-read"]
        set_es_user(username,userInfo)


if __name__ == '__main__':
    excel=r"/sdata/scripts/python3-es/files/elk-user-info.xls"
    userInfo=read_excel(excel)
