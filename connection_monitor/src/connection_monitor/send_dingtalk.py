#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests    
import json
import sys
import os

def sendData(sendURL,atUser,msgtype,typeValue):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    sendValues = {
        "msgtype": msgtype,
        "at": {
            "atMobiles": atUser,
            "isAtALL": False,
        }
    }

    sendValues.update(typeValue)
    r = requests.post(sendURL, data=json.dumps(sendValues), headers=headers)
    return
