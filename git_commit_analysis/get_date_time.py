#! /usr/bin/env python3
from datetime import datetime, date, timedelta

def get_time(delta):
    timeStamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    collectDateTag=(date.today() - timedelta(days=delta)).strftime("%Y-%m-%d")
    startTime=str((date.today() - timedelta(days=delta)).strftime("%m-%d-%Y"))+' 00:00:00'
    endTime=str((date.today() - timedelta(days=(delta-1))).strftime("%m-%d-%Y"))+' 00:00:00'
    return dict(timeStamp=timeStamp,collectDateTag=collectDateTag,startTime=startTime,endTime=endTime)

if __name__ == "__main__":
    delta=7
    print(get_time(delta))
